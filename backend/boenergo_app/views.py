from django.shortcuts import render

from .utils import calculate_square_roots, generate_random_number, generate_random_places, update_items, randomize_items, get_items, get_items_counts
from .forms import SquareRootsForm


def index(request):
    return render(request, 'index.html')


def square_roots(request):
    form = SquareRootsForm(request.POST or None)
    if not form.is_valid():
        return render(request, 'square_roots.html', {'form': form})
    first, second = calculate_square_roots(form.cleaned_data['first'],
                                           form.cleaned_data['second'],
                                           form.cleaned_data['free'])
    context = {
        'form': form,
        'imaginary': form.cleaned_data['imaginary_roots'],
        'root_first': str(first).strip('()'),
        'root_second': str(second).strip('()'),
        'roots_are_equal': first == second,
        'roots_are_imaginary': isinstance(first, complex),
    }
    return render(request, 'square_roots.html', context)


def probability(request):
    if 'reveal' in request.POST:
        update_items(int(request.POST['selected_item']))
    elif 'randomize' in request.POST:
        randomize_items()
    blue, green, red = get_items_counts()
    context = {
        'red': red,
        'green': green,
        'blue': blue,
        'items': get_items(),
        'show_counts': True if 'show_counts' in request.POST else False,
    }
    return render(request, 'probability.html', context)
