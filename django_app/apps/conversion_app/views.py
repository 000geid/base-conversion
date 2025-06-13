from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _, activate

# Helper function to convert to decimal
def to_decimal(number_str, base):
    if base == 'decimal':
        return int(number_str)
    elif base == 'binary':
        return int(number_str, 2)
    elif base == 'octal':
        return int(number_str, 8)
    elif base == 'hexadecimal':
        return int(number_str, 16)
    raise ValueError(_("Invalid base for conversion to decimal."))

# Helper function to convert from decimal
def from_decimal(decimal_number, base):
    if base == 'decimal':
        return str(decimal_number)
    elif base == 'binary':
        return bin(decimal_number)[2:]
    elif base == 'octal':
        return oct(decimal_number)[2:]
    elif base == 'hexadecimal':
        return hex(decimal_number)[2:].upper()
    raise ValueError(_("Invalid base for conversion from decimal."))

def index(request):
    # Activate Spanish language
    activate('es')
    
    context = {
        'number_input': None, 'input_base_selected': 'decimal', 'output_base_selected': 'binary',
        'result': None, 'error': None,
        'calc_number1': None, 'calc_number2': None, 'calc_base_selected': 'decimal',
        'calc_number1_decimal': None, 'calc_number2_decimal': None,
        'calc_operation': None, 'calc_result_original_base': None, 'calc_result_decimal': None,
        'calc_error': None,
        'form_type': None, # To identify which form was submitted
    }

    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        context['form_type'] = form_type

        if form_type == 'base_converter':
            number_input = request.POST.get('number_input')
            input_base = request.POST.get('input_base')
            output_base = request.POST.get('output_base')
            context.update({
                'number_input': number_input, 
                'input_base_selected': input_base, 
                'output_base_selected': output_base
            })

            try:
                if not number_input:
                    raise ValueError(_("Please enter a number to convert."))
                decimal_number = to_decimal(number_input, input_base)
                result = from_decimal(decimal_number, output_base)
                context['result'] = result
            except ValueError as e:
                context['error'] = _("Error converting number: {error_message}. Please check your input and selected bases.").format(error_message=e)
            except Exception as e:
                context['error'] = _("An unexpected error occurred during conversion: {error_message}").format(error_message=e)
        
        elif form_type == 'arithmetic_calculator':
            calc_number1_str = request.POST.get('calc_number1')
            calc_number2_str = request.POST.get('calc_number2')
            calc_base = request.POST.get('calc_base')
            calc_operation = request.POST.get('calc_operation')
            context.update({
                'calc_number1': calc_number1_str, 
                'calc_number2': calc_number2_str, 
                'calc_base_selected': calc_base,
                'calc_operation': calc_operation
            })

            try:
                if not calc_number1_str or not calc_number2_str:
                    raise ValueError(_("Please enter both numbers for calculation."))
                if not calc_operation:
                    raise ValueError(_("Please select an operation."))

                num1_decimal = to_decimal(calc_number1_str, calc_base)
                num2_decimal = to_decimal(calc_number2_str, calc_base)
                context['calc_number1_decimal'] = num1_decimal
                context['calc_number2_decimal'] = num2_decimal
                
                result_decimal = 0
                if calc_operation == 'add':
                    result_decimal = num1_decimal + num2_decimal
                elif calc_operation == 'subtract':
                    result_decimal = num1_decimal - num2_decimal
                elif calc_operation == 'multiply':
                    result_decimal = num1_decimal * num2_decimal
                elif calc_operation == 'divide':
                    if num2_decimal == 0:
                        raise ValueError(_("Division by zero is not allowed."))
                    result_decimal = num1_decimal / num2_decimal # Keep as float for precision
                    # For integer division, you might use // and then decide how to handle non-integer results for non-decimal bases
                else:
                    raise ValueError(_("Invalid operation selected."))

                context['calc_result_decimal'] = result_decimal
                
                # For division, converting float to other bases can be tricky if not an integer.
                # We'll format float to a reasonable precision string for decimal, and handle integer for other bases.
                if calc_operation == 'divide' and not isinstance(result_decimal, int) and calc_base != 'decimal':
                    # If result is float and base is not decimal, it's complex to show in other bases directly.
                    # Option 1: Show error or warning
                    # context['calc_error'] = _("Non-integer division result cannot be directly converted to non-decimal bases.")
                    # context['calc_result_original_base'] = "N/A for non-integer division"
                    # Option 2: Truncate to integer for other bases (might lose precision)
                    context['calc_result_original_base'] = from_decimal(int(result_decimal), calc_base)
                    context['calc_result_decimal'] = f"{result_decimal:.4f}" # Show decimal with precision
                else:
                    context['calc_result_original_base'] = from_decimal(int(result_decimal), calc_base)
                    if isinstance(result_decimal, float):
                         context['calc_result_decimal'] = f"{result_decimal:.4f}"
                    else:
                        context['calc_result_decimal'] = str(int(result_decimal)) # Ensure it's a string

            except ValueError as e:
                context['calc_error'] = _("Error in calculation: {error_message}. Please check your inputs and selected base.").format(error_message=e)
            except Exception as e:
                context['calc_error'] = _("An unexpected error occurred during calculation: {error_message}").format(error_message=e)

    return render(request, 'index.html', context)
