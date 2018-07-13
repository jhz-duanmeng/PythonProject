from collections import OrderedDict

favorite_language = OrderedDict()

favorite_language["jin"] = "python"
favorite_language["david"] = "c++"
favorite_language["phil"] = "ruby"
favorite_language["sarah"] = "python"
favorite_language["ward"] = "android"
favorite_language["kevin"] = "java"

for name, language in favorite_language.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")


