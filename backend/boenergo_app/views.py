from django.shortcuts import render

from .forms import ItemsForm, SquareRootsForm
from .utils import calculate_square_roots, ItemsManager


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
    form = ItemsForm(request.POST or None)
    if form.is_valid():
        ItemsManager.instance().reveal_item(
            int(form.cleaned_data['selected_item'])
        )
    if 'randomize' in request.POST:
        ItemsManager.instance().randomize_items()
    blue, green, red = ItemsManager.instance().get_items_counts()
    context = {
        'form': form,
        'red': red,
        'green': green,
        'blue': blue,
        'items': ItemsManager.instance().get_items(),
        'show_counts': True if 'show_counts' in request.POST else False,
    }
    return render(request, 'probability.html', context)
