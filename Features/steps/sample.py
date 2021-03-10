from lib2to3.fixes.fix_input import context

# from Features.steps.Environment import before_all

def before_all(context):
    print("this is my all before all")

def after_all(context):
    print("this")

def before_scenario(context,scenario):
    print("this")