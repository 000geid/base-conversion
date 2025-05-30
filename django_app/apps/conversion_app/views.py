from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _

# Create your views here.
def index(request):
    context = {}
    if request.method == 'POST':
        number_input = request.POST.get('number_input')
        input_base = request.POST.get('input_base')
        output_base = request.POST.get('output_base')

        try:
            # Convert input number to decimal first
            if input_base == 'decimal':
                decimal_number = int(number_input)
            elif input_base == 'binary':
                decimal_number = int(number_input, 2)
            elif input_base == 'octal':
                decimal_number = int(number_input, 8)
            elif input_base == 'hexadecimal':
                decimal_number = int(number_input, 16)
            else:
                # This specific error message is for invalid dropdown values, not user input directly.
                # It might be better to keep it as is or handle it differently if it needs translation.
                raise ValueError("Invalid input base selected by the user.") 

            # Convert decimal number to output base
            if output_base == 'decimal':
                result = str(decimal_number)
            elif output_base == 'binary':
                result = bin(decimal_number)[2:]
            elif output_base == 'octal':
                result = oct(decimal_number)[2:]
            elif output_base == 'hexadecimal':
                result = hex(decimal_number)[2:]
            else:
                raise ValueError("Invalid output base selected by the user.")
            
            context['result'] = result
        except ValueError as e:
            # The core of the error `e` (e.g., "invalid literal for int() with base 2: 'abc'") is from Python and not easily translatable directly.
            # We translate our surrounding message.
            context['error'] = _("Error converting number: {error_message}. Please enter a valid number for the selected input base.").format(error_message=e)
        except Exception as e:
            context['error'] = _("An unexpected error occurred: {error_message}").format(error_message=e)
        
        context['number_input'] = number_input
        context['input_base_selected'] = input_base
        context['output_base_selected'] = output_base

    return render(request, 'index.html', context)
