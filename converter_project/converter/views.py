from django.shortcuts import render
from django.http import HttpResponse

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
                raise ValueError("Invalid input base")

            # Convert decimal number to output base
            if output_base == 'decimal':
                result = str(decimal_number)
            elif output_base == 'binary':
                result = bin(decimal_number)[2:]  # [2:] to remove "0b" prefix
            elif output_base == 'octal':
                result = oct(decimal_number)[2:]  # [2:] to remove "0o" prefix
            elif output_base == 'hexadecimal':
                result = hex(decimal_number)[2:]  # [2:] to remove "0x" prefix
            else:
                raise ValueError("Invalid output base")
            
            context['result'] = result
        except ValueError as e:
            context['error'] = f"Error: {e}. Please enter a valid number for the selected input base."
        except Exception as e:
            context['error'] = f"An unexpected error occurred: {e}"
        
        context['number_input'] = number_input
        context['input_base_selected'] = input_base
        context['output_base_selected'] = output_base


    return render(request, 'index.html', context)
