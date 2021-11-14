# Laba No7 -- Task 2
# Завдання  2:  Зобразити  гістограму  частоти  появи  літер  у  певному  тексті  та 
# зберегти у .png файл

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec non pretium diam. Nam sollicitudin dui quis hendrerit laoreet. Quisque sagittis volutpat purus eu lacinia. Aenean accumsan vitae odio eu ultrices. Quisque condimentum porttitor nisi, eu maximus velit tincidunt tempor. Curabitur ultrices pellentesque sollicitudin. Interdum et malesuada fames ac ante ipsum primis in faucibus. Vivamus ac neque non lacus mollis efficitur eget id nunc. Proin pellentesque est nisl, eget tristique nisl sodales sit amet. Aliquam sed arcu enim. Curabitur a sem erat. Proin sagittis dolor ac ligula euismod, at suscipit tellus consequat. Quisque accumsan nisi risus, eget aliquam mauris bibendum sit amet. Sed id fermentum enim. Vivamus quis suscipit dui. Aliquam ac nisi elementum, mattis quam in, laoreet massa. Phasellus non suscipit magna, blandit placerat tortor. Vivamus at tristique tellus. Curabitur dolor lacus, ultricies et odio eget, pretium tempor massa. Nulla scelerisque malesuada semper. Mauris est risus, porta ac ornare nec, facilisis nec neque. Integer vitae feugiat diam. Quisque vestibulum enim commodo ipsum vestibulum, a congue arcu lacinia. Duis metus ex, posuere vitae tincidunt quis, tincidunt a neque. Proin condimentum lorem vitae maximus faucibus. Aenean molestie euismod eros vel iaculis. Vivamus non nisi ut lectus auctor commodo. Morbi convallis cursus quam, quis cursus dolor ultricies at. Donec efficitur enim turpis, quis suscipit odio dignissim et. Donec tincidunt, tellus id iaculis vehicula, lacus lacus mattis tellus, at convallis ligula quam in enim. Vivamus sed tincidunt nunc. Maecenas cursus ut lectus vitae sagittis. Proin vehicula rhoncus lorem a sodales. Maecenas mollis orci eu lectus faucibus accumsan. In quis suscipit urna. Maecenas aliquam, nunc sit amet mollis laoreet, lacus elit imperdiet tortor, elementum volutpat massa justo vel ipsum. Vestibulum quis nulla porttitor, facilisis neque sed, fermentum urna. Donec dapibus vitae libero vitae auctor. Cras arcu quam, dictum at lorem et, auctor euismod magna. Mauris tristique aliquam metus eu luctus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Fusce magna eros, gravida eget risus ac, tempor interdum turpis. Suspendisse potenti. Praesent faucibus sagittis faucibus. Aliquam facilisis odio vel dui consectetur, maximus ullamcorper est venenatis. Morbi elementum, arcu eu tincidunt consequat, enim sapien tempor augue, lacinia sodales felis arcu sit amet nisl. Proin et laoreet libero. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Mauris congue nisi id tellus placerat molestie. Ut finibus massa non ipsum aliquam, nec hendrerit purus semper. Proin mauris quam, imperdiet vel eros eu, dapibus vehicula mi. Nunc sagittis arcu dolor, vel elementum nisi eleifend eget. Quisque augue ex, viverra viverra euismod nec, condimentum sed metus. Aenean in quam id metus aliquet porta. Donec eros ante, pulvinar eu sapien in, gravida feugiat tellus. Vivamus fringilla diam at magna ultrices imperdiet. Vestibulum eget convallis sapien.".upper()

lettersCount = {i:text.count(i) for i in text}
del lettersCount[" "]
del lettersCount["."]
del lettersCount[","]

import pylab
import sys

xdata = list(lettersCount.keys())
xdata.sort()
ydata = [lettersCount[i] for i in xdata]
pylab.bar(xdata, ydata) 
pylab.title("Lorem ipsum dolor, 500 chars")
pylab.savefig(sys.path[0]+"/figOutputTask2.png")