from django.shortcuts import render
from .forms import InputForm
import math

def calculate_view(request):
    result = None
    error = None

    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            try:
                a = form.cleaned_data['a']
                b = form.cleaned_data['b']
                c = form.cleaned_data['c']

                if a < 1:
                    error = "Value A is too small. Must be at least 1."
                elif c < 0:
                    error = "Value C cannot be negative."
                else:
                    c_cubed = c ** 3
                    if c_cubed > 1000:
                        result = math.sqrt(c_cubed) * 10
                    else:
                        if a == 0:
                            error = "Cannot divide by zero (Value A)."
                        else:
                            result = math.sqrt(c_cubed) / a
                    if result is not None:
                        result += b
                    if b == 0:
                        result = f"{result:.2f} (Note: B was zero, so no impact on result)"
            except Exception as e:
                error = f"An error occurred: {str(e)}"
        else:
            error = "Invalid input. Please enter valid numbers."
    else:
        form = InputForm()

    return render(request, 'calculator/result.html', {
        'form': form,
        'result': result,
        'error': error
    })
