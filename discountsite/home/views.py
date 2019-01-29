from django.shortcuts import render
from django.http import HttpResponse
import discountsite.common as com
from discountsite.common import asos, uniqlo, gap, handm
def index(request):
    context = {}
    if request.method == 'POST':
        # master_array = [['bag2', 'https/link', 'https/img', '$45.00', '$25.00'], ['bag1', 'https', 'https', '$45.00', '$15.00']]
        search_input = request.POST.get('search input', None)
        master_array = []
        master_array += asos.search(search_input)
        master_array += uniqlo.search(search_input)
        master_array += gap.search(search_input)
        # master_array += handm.search(search_input)
        master_array = sort(master_array)
        context['master'] = master_array
        return render(request, 'home/index.html', context)
    else:
        return render(request, 'home/index.html', context)
    return render(request, 'home/index.html', context)


def sort(master_array):
    new_arr = []
    link_arr = []
    for arr in master_array:
        if arr[1] not in link_arr:
            new_arr.append(arr)
    for arr in new_arr:
        arr += [int(((float(arr[3][1:])-float(arr[4][1:]))/float(arr[3][1:]))*100)]
    master_array = sorted(master_array, key=lambda x:x[6], reverse=True)
    return master_array


