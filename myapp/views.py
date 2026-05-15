from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    tags = requests.get("https://dummyjson.com/recipes/tags").json()
    url = requests.get("https://dummyjson.com/recipes")
    response = url.json()
    data = response["recipes"]
    context = {
        "data":data,
        "tags":tags,
    }
    return render(request,"index.html",context)

def databytags(request,tags):
    print(tags)
    response = requests.get(f"https://dummyjson.com/recipes/tag/{tags}").json()
    tags = requests.get("https://dummyjson.com/recipes/tags").json()

    data=response["recipes"]
    context = {
        "data":data,
        "tags":tags,
    }
    return render(request,"index.html",context)

def mealtype(request,meal):
    response = requests.get(f"https://dummyjson.com/recipes/meal-type/{meal}").json()
    tags = requests.get("https://dummyjson.com/recipes/tags").json()
    data=response["recipes"]
    context = {
        "data": data,
        "tags": tags,
    }
    return render(request,"index.html",context)

def search(request):
    userquery = request.POST.get("query")
    print(userquery)
    response = requests.get(f"https://dummyjson.com/recipes/search?q={userquery}").json()

    tags = requests.get("https://dummyjson.com/recipes/tags").json()
    data = response["recipes"]
    context = {
        "data": data,
        "tags": tags,
    }
    return render(request,"index.html",context)

def singlepage(request,id):
    print(id)
    response = requests.get(f"https://dummyjson.com/recipes/{id}").json()
    # Fetch more recipes for the "More Recipes" section
    all_recipes = requests.get("https://dummyjson.com/recipes?limit=50").json()
    recommended = [r for r in all_recipes["recipes"] if r["id"] != id][:3]
    context = {
        "data":response,
        "recommended": recommended,
    }
    return render(request,"receipes.html",context)