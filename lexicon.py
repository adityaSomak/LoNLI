import checklist
from checklist.editor import Editor
editor = Editor()

lexicons = {}
lexicons['MALE_NAME'] = [nm for i,nm in enumerate(editor.lexicons['first_name']) if i % 2 == 0][:100]
lexicons['FEMALE_NAME'] = [nm for i,nm in enumerate(editor.lexicons['first_name']) if i % 2 == 1][:100]
lexicons['NAME'] = lexicons['MALE_NAME'] + lexicons['FEMALE_NAME']
lexicons['TURN'] = ['back','left','right']
lexicons['DIRECTION'] = ['North','South','East','West']
lexicons['FRUIT'] = ["apple","apricot","avocado","banana","blackberry","blueberry","cherry","coconut","cucumber","durian","dragonfruit","fig","gooseberry","grape","guava","jackfruit","plum","kiwifruit","kumquat","lemon","lime","mango","watermelon","mulberry","orange","papaya","passionfruit","peach","pear","persimmon","pineapple","pineberry","quince","raspberry","soursop","star fruit","strawberry","tamarind","yuzu"]
lexicons['COLOUR'] = ['red','green','yellow','blue','magenta','purple','crimson','maroon','brown','white','pink','black','grey']
lexicons['SCHOOL_ENTITY'] = ['class', 'school', 'university', 'college']
lexicons['SCHOOL_NOUN'] = ['student', 'boy', 'girl', 'teacher', 'professor']
lexicons['EMOTION'] = ['happy','sad','delighted','surprised','angry','amused','content']
lexicons['KNOW'] = ['knew', 'didn\'t know']
lexicons['LOCATION'] = ['school', 'museum', 'park', 'hotel', 'hospital', 'office', 'theatre']
lexicons['PROFESSION'] = ["writer","author","engineer","teacher","physician","accountant","architect","lawyer","electrician","librarian","cook","secretary","dentist","dietitian","mechanic","chef","actor","plumber","firefighter","aviator","designer","police officer","journalist","hairdresser","artist","economist","tailor","butler","farmer","judge","lecturer","professor","model","nurse","photographer","scientist"]
lexicons['ANIMAL'] = ["alligator","bear","bison","buffalo","camel","cat","cheetah","cow","deer","dog","donkey","elephant","fox","goat","hippopotamus","horse","kangaroo","leopard","lion","llama","mongoose","monkey","moose","mouse","mule","ostrich","otter","ox","panda","penguin","pig","polar bear","rabbit","raccoon","rat","sheep","snail","snake","tiger","wolf","zebra"]
lexicons['OBJECT_TABLE'] = ['cup','glass','plate','silverware','fork','knife','spoon','bowl','coaster','bottle','food','pitcher','serviette','napkin','snack','cookie','key','pin','file','mousepad','flower pot','book','notebook','laptop','phone','perfume','eyeliner','face wash','toothbrush','toothpaste']
lexicons['ADJECTIVE_OF_PERSON'] = ['able','abnormal','above average','absent-minded','adventurous','affectionate','agile','agreeable','alert','amazing','ambitious','amiable','amusing','analytical','angelic','apathetic','apprehensive','ardent','artificial','artistic','assertive','attentive','average','awesome','awful','balanced','beautiful','below average','beneficent','blue','blunt','boisterous','brave','bright','brilliant','buff','callous','candid','cantankerous','capable','careful','careless','caustic','cautious','charming','cheerful','chic','childish','childlike','churlish','circumspect','civil','clean','clever','clumsy','coherent','cold','competent','composed','conceited','condescending','confident','confused','conscientious','considerate','content','cool','cool-headed','cooperative','cordial','courageous','cowardly','crabby','crafty','cranky','crass','critical','cruel','curious','cynical','dainty','decisive','deep','deferential','deft','delicate','delightful','demonic','demure','dependent','depressed','devoted','dextrous','diligent','direct','dirty','disagreeable','discerning','discreet','disruptive','distant','distraught','distrustful','dowdy','dramatic','dreary','drowsy','drugged','drunk','dull','dutiful','eager','earnest','easy-going','efficient','egotistical','elfin','emotional','energetic','enterprising','enthusiastic','evasive','even-tempered','exacting','excellent','excitable','experienced','fabulous','fastidious','ferocious','fervent','fiery','flabby','flaky','flashy','frank','friendly','funny','fussy','generous','gentle','gloomy','gluttonous','good','grave','great','groggy','grouchy','guarded','hateful','hearty','helpful','hesitant','hot-headed','hypercritical','hysterical','idiotic','idle','illogical','imaginative','immature','immodest','impatient','imperturbable','impetuous','impractical','impressionable','impressive','impulsive','inactive','incisive','incompetent','inconsiderate','inconsistent','indefatigable','independent','indiscreet','indolent','industrious','inexperienced','insensitive','inspiring','intelligent','interesting','intolerant','inventive','irascible','irritable','irritating','jocular','jovial','joyous','judgmental','keen','kind','lame','lazy','lean','leery','lethargic','level-headed','listless','lithe','lively','local','logical','long-winded','lovable','love-lorn','lovely','maternal','mature','mean','meddlesome','mercurial','methodical','meticulous','mild','miserable','modest','moronic','morose','motivated','musical','naive','nasty','natural','naughty','negative','nervous','noisy','normal','nosy','numb','obliging','obnoxious','old-fashioned','one-sided','orderly','ostentatious','outgoing','outspoken','passionate','passive','paternal','paternalistic','patient','peaceful','peevish','pensive','persevering','persnickety','petulant','picky','plain','plain-speaking','playful','pleasant','plucky','polite','popular','positive','powerful','practical','prejudiced','pretty','proficient','proud','provocative','prudent','punctual','quarrelsome','querulous','quick','quick-tempered','quiet','realistic','reassuring','reclusive','reliable','reluctant','resentful','reserved','resigned','resourceful','respected','respectful','responsible','restless','revered','ridiculous','sad','sassy','saucy','sedate','self-assured','selfish','sensible','sensitive','sentimental','serene','serious','sharp','short-tempered','shrewd','shy','silly','sincere','sleepy','slight','sloppy','slothful','slovenly','slow','smart','snazzy','sneering','snobby','sober','somber','sophisticated','soulful','soulless','sour','spirited','spiteful','stable','staid','steady','stern','stoic','striking','strong','stupid','sturdy','subtle','sulky','sullen','supercilious','superficial','surly','suspicious','sweet','tactful','tactless','talented','testy','thinking','thoughtful','thoughtless','timid','tired','tolerant','touchy','tranquil','ugly','unaffected','unbalanced','uncertain','uncooperative','undependable','unemotional','unfriendly','unguarded','unhelpful','unimaginative','unmotivated','unpleasant','unpopular','unreliable','unsophisticated','unstable','unsure','unthinking','unwilling','venal','versatile','vigilant','volcanic','vulnerable','warm','warmhearted','wary','watchful','weak','well-behaved','well-developed','well-intentioned','well-respected','well-rounded','willing','wonderful','zealous']
lexicons['CITY'] = ['Houston','Irvine','Irving','Kansas','Las Vegas','Manchester','Miami','Minneapolis','Ontario','Pittsburg','Rochester','Springfield','Tempe','Tulsa','Boston','Illinois','Washington','Hartford','Phoenix','Frankfurt','Albany','San Francisco','San Jose','Sacramento','Los Angeles','Oklahoma','Columbia','Richmond','Olympia','Madison','Chicago','New York','Philadelphia','Dallas','San Diego','Santa Barbara','Buffalo','Detroit','Hampton']
lexicons['CONTINUOUS_VERB'] = ['painting','reading','swimming','dancing','sleeping','studying','running','exercising','writing','speaking','listening','travelling','going','working']
lexicons['SUBJECT'] = ['history','geography','mathematics','physics','chemistry','biology','economics','geology','political science','music','commerce','computer science','literature','art','latin','french']
lexicons['LOCATION_HOUSE'] = ['bedroom','kitchen','living room','bathroom','study room','terrace','dining room','store room','basement']
lexicons['NEGATION_ADVERB'] = ['hardly','rarely','seldom','scarcely']
lexicons['OBJECT'] = ['diary', 'bottle', 'car', 'tissue', 'glass', 'watch', 'photo', 'camera', 'stamp', 'postcard', 'dictionary', 'coin', 'brush', 'credit card', 'identity card', 'mobile phone', 'wallet', 'button', 'umbrella', 'pen', 'pencil', 'lighter', 'cigarette', 'match', 'lipstick', 'purse', 'case', 'clip', 'scissor', 'rubber', 'file', 'banknote', 'comb', 'notebook', 'laptop', 'mirror', 'toothbrush', 'headphone', 'player', 'battery', 'light bulb', 'newspaper', 'magazine', 'alarm clock']
lexicons['OBJECTS'] = ['diaries', 'bottles', 'cars', 'tissues', 'glasses', 'watches', 'photos', 'cameras', 'stamps', 'postcards', 'dictionaries', 'coins', 'brushes', 'credit cards', 'identity cards', 'mobile phones', 'wallets', 'buttons', 'umbrellas', 'pens', 'pencils', 'lighters', 'cigarettes', 'matches', 'lipsticks', 'purses', 'cases', 'clips', 'scissors', 'rubbers', 'files', 'banknotes', 'combs', 'notebooks', 'laptops', 'mirrors', 'toothbrushes', 'headphones', 'players', 'batteries', 'light bulbs', 'newspapers', 'magazines', 'alarm clocks']

lexicons['N'] = list([str(i) for i in range(1,11,1)])
lexicons['YEAR'] = list([str(i) for i in range(1990,2021,1)])
lexicons['TIME'] = ['6 AM','6:30 AM','7 AM','7:30 AM','8 AM','8:30 AM','9 AM','9:30 AM','10 AM', '10:30 AM', '11 AM', '11:30 AM','12 noon','12:30 PM','1 PM','1:30 PM','2 PM','2:30 PM','3 PM','3:30 PM','4 PM','4:30 PM','5 PM','5:30 PM','6 PM']
lexicons['MILE'] = list([str(i) for i in range(200,1000,5)])
lexicons['DOLLAR'] = ['10', '20', '30', '40', '50', '100', '200', '300', '400', '500', '1000']

lexicons['T0_SYN_ANT'] = [("alien","foreigner","resident"),("authentic","accurate","unreal"),("awkward","rude","adroit"),("barbarous","frustrate","civilized"),("brittle","breakable","tough"),("bawdy","coarse","decent"),("batty","silly","sane"),("benevolent","generous","malevolent"),("benign","favorable","malignant"),("busy","active","idle"),("bold","adventurous","timid"),("blunt","insensitive","keen"),("callous","unfeeling","compassionate"),("capable","competent","incompetent"),("calculating","devious","artless"),("chaste","virtuous","lustful"),("callous","insensitive","kind"),("calm","harmonious","stormy"),("candid","blunt","evasive"),("celebrated","acclaimed","unknown"),("cheap","competitive","dear"),("coarse","bawdy","fine"),("classic","simple","unusual"),("comic","clown","tragic"),("confident","bold","diffident"),("docile","pliable","headstrong"),("destructive","catastrophic","creative"),("dwarf","diminutive","huge"),("eager","keen","indifferent"),("eccentric","strange","natural"),("enormous","colossal","diminutive"),("equivocal","uncertain","obvious"),("fanatical","narrow-minded","liberal"),("feeble","weak","strong"),("fragile","weak","enduring"),("frivolous","petty","solemn"),("frantic","violent","subdued"),("gorgeous","magnificent","dull"),("gracious","courteous","rude"),("genuine","absolute","spurious"),("gloomy","bleak","gay"),("haughty","arrogant","humble"),("hasty","abrupt","leisurely"),("humble","meek","proud"),("indifferent","equitable","partial"),("impulsive","flaky","cautious"),("indigent","destitute","rich"),("interesting","enchanting","dull"),("imminent","impending","distant"),("impartial","just","prejudiced"),("impious","irreligious","pious"),("incompetent","inefficient","dexterous"),("invincible","unconquerable","effeminate"),("irrepressible","irresistible","composed"),("jaded","tired","renewed"),("jubilant","rejoicing","melancholy"),("jovial","frolicsome","solemn"),("just","honest","unequal"),("judicious","thoughtful","irrational"),("juvenile","young","dotage"),("keen","sharp","vapid"),("lavish","abundant","scarce"),("liable","accountable","unaccountable"),("lenient","compassionate","cruel"),("lucid","sound","obscure"),("liberal","magnanimous","stingy"),("luxuriant","profuse","scanty"),("masculine","gallant","feminine"),("modest","humble","arrogant"),("monotonous","irksome","varied"),("novice","tyro","veteran"),("nonchalant","indifferent","attentive"),("offensive","abhorrent","engaging"),("optimist","idealist","pessimist"),("placid","tranquil","turbulent"),("precarious","doubtful","assured"),("pompous","haughty","unpretentious"),("quaint","queer","familiar"),("rebellious","restless","submissive"),("reluctant","cautious","anxious"),("ruthless","remorseless","compassionate"),("savage","wild","polished"),("sacred","cherish","ungodly"),("stranger","immigrant","acquaintance"),("sarcastic","ironical","courteous"),("shrewd","cunning","simple"),("successful","propitious","destitute"),("sycophant","parasite","devoted"),("superficial","partial","profound"),("taciturn","reserved","talkative"),("tenacious","stubborn","docile"),("timid","diffident","bold"),("tranquil","peaceful","violent"),("treacherous","dishonest","forthright"),("trenchant","assertive","feeble"),("tumultuous","violent","peaceful"),("thrifty","frugal","extravagant"),("transparent","diaphanous","opaque"),("vagrant","wander","steady"),("venerable","honored","unworthy"),("vigilant","cautious","careless"),("vouch","confirm","prohibit"),("wicked","immoral","noble"),("winsome","beautiful","alluring")]
lexicons['T1_POS_COM_SUP'] = [('angry','angrier','angriest'),('bad','worse','worst'),('bitter','bitterer','bitterest'),('big','bigger','biggest'),('bold','bolder','boldest'),('bossy','bossier','bossiest'),('brave','braver','bravest'),('bright','brighter','brightest'),('busy','busier','busiest'),('calm','calmer','calmest'),('chubby','chubbier','chubbiest'),('classy','classier','classiest'),('clever','cleverer','cleverest'),('clumsy','clumsier','clumsiest'),('crazy','crazier','craziest'),('creepy','creepier','creepiest'),('cruel','crueller','cruellest'),('cute','cuter','cutest'),('curvy','curvier','curviest'),('dense','denser','densest'),('dull','duller','dullest'),('dumb','dumber','dumbest'),('fair','fairer','fairest'),('fat','fatter','fattest'),('fast','faster','fastest'),('firm','firmer','firmest'),('friendly','friendlier','friendliest'),('funny','funnier','funniest'),('fit','fitter','fittest'),('good','better','best'),('gentle','gentler','gentlest'),('gloomy','gloomier','gloomiest'),('greedy','greedier','greediest'),('great','greater','greatest'),('guilty','guilter','guiltiest'),('gross','grosser','grossest'),('happy','happier','happiest'),('hairy','hairier','hairiest'),('healthy','healthier','healthiest'),('harsh','harsher','harshest'),('hungry','hungrier','hungriest'),('humble','humbler','humblest'),('hot','hotter','hottest'),('kind','kinder','kindest'),('lazy','lazier','laziest'),('long','longer','longest'),('lovely','lovelier','loveliest'),('lonely','lonlier','loneliest'),('loud','louder','loudest'),('mean','meaner','meanest'),('messy','messier','messiest'),('naughty','naughtier','naughtiest'),('nice','nicer','nicest'),('noisy','noisier','noisiest'),('old','older','oldest'),('polite','politer','politest'),('poor','poorer','poorest'),('proud','prouder','proudest'),('pretty','prettier','prettiest'),('quiet','quieter','quietest'),('rich','richer','richest'),('rude','ruder','rudest'),('sad','sadder','saddest'),('salty','saltier','saltiest'),('shallow','shallower','shallowest'),('scary','scarier','scariest'),('sharp','sharper','sharpest'),('short','shorter','shortest'),('silly','sillier','silliest'),('shy','shyer','shyest'),('sincere','sincerer','sincerest'),('sleepy','sleepier','sleepiest'),('skinny','skinnier','skinniest'),('slow','slower','slowest'),('slim','slimmer','slimmest'),('small','smaller','smallest'),('smart','smarter','smartest'),('sorry','sorrier','sorriest'),('strong','stronger','strongest'),('sweet','sweeter','sweetest'),('tall','taller','tallest'),('thin','thinner','thinnest'),('tiny','tinier','tiniest'),('tough','tougher','toughest'),('ugly','uglier','ugliest'),('wealthy','wealthier','wealthiest'),('weird','weirder','weirdest'),('weak','weaker','weakest'),('wise','wiser','wisest'),('young','younger','youngest'),('renowned','more renowned','most renowned'),('popular','more popular','most popular'),('modern','more modern','most modern'),('beautiful','more beautiful','most beautiful'),('interesting','more interesting','most interesting'),('important','more important','most important'),('handsome','more handsome','most handsome'),('attractive','more attractive','most attractive'),('polite','more polite','most polite'),('bitter','more bitter','most bitter'),('clever','more clever','most clever'),('tired','more tired','most tired')]
lexicons['T2_POS_COM_SUP_MISMATCH'] = [('kind','kinder','kindest','hungry','hungrier','hungriest'),('sweet','sweeter','sweetest','greedy','greedier','greediest'),('cruel','crueller','cruellest','healthy','healthier','healthiest'),('bright','brighter','brightest','sorry','sorrier','sorriest'),('great','greater','greatest','guilty','guilter','guiltiest'),('dense','denser','densest','hungry','hungrier','hungriest'),('lazy','lazier','laziest','small','smaller','smallest'),('fair','fairer','fairest','funny','funnier','funniest'),('small','smaller','smallest','important','more important','most important'),('short','shorter','shortest','wealthy','wealthier','wealthiest'),('big','bigger','biggest','poor','poorer','poorest'),('loud','louder','loudest','tired','more tired','most tired'),('noisy','noisier','noisiest','sad','sadder','saddest'),('great','greater','greatest','kind','kinder','kindest'),('short','shorter','shortest','modern','more modern','most modern'),('curvy','curvier','curviest','lazy','lazier','laziest'),('short','shorter','shortest','dense','denser','densest'),('cruel','crueller','cruellest','weak','weaker','weakest'),('firm','firmer','firmest','old','older','oldest'),('modern','more modern','most modern','pretty','prettier','prettiest'),('shallow','shallower','shallowest','hungry','hungrier','hungriest'),('hungry','hungrier','hungriest','wealthy','wealthier','wealthiest'),('hairy','hairier','hairiest','clever','more clever','most clever'),('slow','slower','slowest','firm','firmer','firmest'),('wealthy','wealthier','wealthiest','fair','fairer','fairest'),('sharp','sharper','sharpest','ugly','uglier','ugliest'),('wise','wiser','wisest','tired','more tired','most tired'),('skinny','skinnier','skinniest','polite','more polite','most polite'),('fair','fairer','fairest','chubby','chubbier','chubbiest'),('thin','thinner','thinnest','messy','messier','messiest'),('sorry','sorrier','sorriest','important','more important','most important'),('curvy','curvier','curviest','hairy','hairier','hairiest'),('hungry','hungrier','hungriest','dumb','dumber','dumbest'),('mean','meaner','meanest','old','older','oldest'),('old','older','oldest','chubby','chubbier','chubbiest'),('hairy','hairier','hairiest','good','better','best'),('fair','fairer','fairest','old','older','oldest'),('bitter','more bitter','most bitter','old','older','oldest'),('messy','messier','messiest','poor','poorer','poorest'),('funny','funnier','funniest','sharp','sharper','sharpest'),('hairy','hairier','hairiest','gloomy','gloomier','gloomiest'),('pretty','prettier','prettiest','sincere','sincerer','sincerest'),('fast','faster','fastest','polite','more polite','most polite'),('sharp','sharper','sharpest','hairy','hairier','hairiest'),('silly','sillier','silliest','small','smaller','smallest'),('sharp','sharper','sharpest','renowned','more renowned','most renowned'),('fast','faster','fastest','sleepy','sleepier','sleepiest'),('shy','shyer','shyest','chubby','chubbier','chubbiest'),('dense','denser','densest','nice','nicer','nicest'),('short','shorter','shortest','humble','humbler','humblest'),('attractive','more attractive','most attractive','gentle','gentler','gentlest'),('bright','brighter','brightest','dumb','dumber','dumbest'),('healthy','healthier','healthiest','messy','messier','messiest'),('old','older','oldest','hairy','hairier','hairiest'),('busy','busier','busiest','young','younger','youngest'),('important','more important','most important','firm','firmer','firmest'),('strong','stronger','strongest','guilty','guilter','guiltiest'),('fit','fitter','fittest','dull','duller','dullest'),('slow','slower','slowest','salty','saltier','saltiest'),('loud','louder','loudest','hot','hotter','hottest'),('messy','messier','messiest','old','older','oldest'),('poor','poorer','poorest','rude','ruder','rudest'),('firm','firmer','firmest','sharp','sharper','sharpest'),('slow','slower','slowest','crazy','crazier','craziest'),('tired','more tired','most tired','silly','sillier','silliest'),('cruel','crueller','cruellest','sincere','sincerer','sincerest'),('strong','stronger','strongest','curvy','curvier','curviest'),('renowned','more renowned','most renowned','strong','stronger','strongest'),('bitter','bitterer','bitterest','short','shorter','shortest'),('lazy','lazier','laziest','popular','more popular','most popular'),('nice','nicer','nicest','interesting','more interesting','most interesting'),('clever','more clever','most clever','polite','politer','politest'),('bad','worse','worst','clever','cleverer','cleverest'),('gross','grosser','grossest','sharp','sharper','sharpest'),('hungry','hungrier','hungriest','clever','cleverer','cleverest'),('important','more important','most important','ugly','uglier','ugliest'),('lazy','lazier','laziest','rich','richer','richest'),('smart','smarter','smartest','renowned','more renowned','most renowned'),('noisy','noisier','noisiest','dense','denser','densest'),('hot','hotter','hottest','naughty','naughtier','naughtiest'),('silly','sillier','silliest','attractive','more attractive','most attractive'),('funny','funnier','funniest','short','shorter','shortest'),('sad','sadder','saddest','classy','classier','classiest'),('pretty','prettier','prettiest','long','longer','longest'),('pretty','prettier','prettiest','bright','brighter','brightest'),('renowned','more renowned','most renowned','interesting','more interesting','most interesting'),('dense','denser','densest','small','smaller','smallest'),('modern','more modern','most modern','mean','meaner','meanest'),('weak','weaker','weakest','sharp','sharper','sharpest'),('sad','sadder','saddest','wise','wiser','wisest'),('poor','poorer','poorest','fat','fatter','fattest'),('fast','faster','fastest','polite','politer','politest'),('small','smaller','smallest','tired','more tired','most tired'),('small','smaller','smallest','sweet','sweeter','sweetest'),('cruel','crueller','cruellest','firm','firmer','firmest'),('long','longer','longest','hot','hotter','hottest'),('wise','wiser','wisest','small','smaller','smallest'),('skinny','skinnier','skinniest','polite','politer','politest'),('dumb','dumber','dumbest','lazy','lazier','laziest'),('sorry','sorrier','sorriest','hairy','hairier','hairiest'),('tired','more tired','most tired','sad','sadder','saddest'),('busy','busier','busiest','small','smaller','smallest'),('cute','cuter','cutest','bitter','more bitter','most bitter'),('chubby','chubbier','chubbiest','dense','denser','densest'),('bitter','bitterer','bitterest','skinny','skinnier','skinniest'),('slow','slower','slowest','handsome','more handsome','most handsome'),('renowned','more renowned','most renowned','skinny','skinnier','skinniest'),('bossy','bossier','bossiest','lonely','lonlier','loneliest'),('guilty','guilter','guiltiest','fit','fitter','fittest'),('beautiful','more beautiful','most beautiful','tired','more tired','most tired'),('clever','cleverer','cleverest','shallow','shallower','shallowest'),('beautiful','more beautiful','most beautiful','short','shorter','shortest'),('strong','stronger','strongest','funny','funnier','funniest'),('sincere','sincerer','sincerest','clumsy','clumsier','clumsiest'),('clever','more clever','most clever','wealthy','wealthier','wealthiest'),('happy','happier','happiest','sincere','sincerer','sincerest'),('sorry','sorrier','sorriest','brave','braver','bravest'),('wealthy','wealthier','wealthiest','sorry','sorrier','sorriest'),('short','shorter','shortest','cute','cuter','cutest'),('big','bigger','biggest','fat','fatter','fattest'),('harsh','harsher','harshest','modern','more modern','most modern'),('tough','tougher','toughest','gentle','gentler','gentlest'),('classy','classier','classiest','crazy','crazier','craziest'),('guilty','guilter','guiltiest','pretty','prettier','prettiest'),('dense','denser','densest','crazy','crazier','craziest'),('sleepy','sleepier','sleepiest','nice','nicer','nicest'),('weak','weaker','weakest','busy','busier','busiest'),('fat','fatter','fattest','kind','kinder','kindest'),('noisy','noisier','noisiest','messy','messier','messiest'),('lonely','lonlier','loneliest','sweet','sweeter','sweetest'),('angry','angrier','angriest','beautiful','more beautiful','most beautiful'),('sweet','sweeter','sweetest','popular','more popular','most popular'),('sincere','sincerer','sincerest','tired','more tired','most tired'),('fair','fairer','fairest','dumb','dumber','dumbest'),('brave','braver','bravest','fit','fitter','fittest'),('harsh','harsher','harshest','slim','slimmer','slimmest'),('noisy','noisier','noisiest','firm','firmer','firmest'),('quiet','quieter','quietest','interesting','more interesting','most interesting'),('bitter','bitterer','bitterest','ugly','uglier','ugliest'),('modern','more modern','most modern','sleepy','sleepier','sleepiest'),('loud','louder','loudest','scary','scarier','scariest'),('proud','prouder','proudest','calm','calmer','calmest'),('popular','more popular','most popular','rude','ruder','rudest'),('brave','braver','bravest','crazy','crazier','craziest'),('scary','scarier','scariest','popular','more popular','most popular'),('silly','sillier','silliest','messy','messier','messiest'),('curvy','curvier','curviest','tiny','tinier','tiniest'),('wealthy','wealthier','wealthiest','busy','busier','busiest'),('bright','brighter','brightest','chubby','chubbier','chubbiest'),('great','greater','greatest','skinny','skinnier','skinniest'),('young','younger','youngest','clever','cleverer','cleverest'),('sorry','sorrier','sorriest','gloomy','gloomier','gloomiest'),('dense','denser','densest','tiny','tinier','tiniest'),('polite','politer','politest','friendly','friendlier','friendliest'),('hot','hotter','hottest','noisy','noisier','noisiest'),('curvy','curvier','curviest','polite','more polite','most polite'),('tall','taller','tallest','ugly','uglier','ugliest')]
lexicons['T3_COM_ANTONYM'] = [('smarter','dumber'),('stronger','weaker'),('older','younger'),('tinier','bigger'),('bigger','tinier'),('tougher','softer'),('taller','shorter'),('younger','elder'),('faster','slower'),('nicer','ruder'),('shorter','taller'),('weaker','stronger'),('richer','poorer'),('quicker','slower'),('happier','sadder'),('slower','faster'),('heavier','lighter'),('quieter','louder'),('thinner','fatter'),('louder','quieter'),('wealthier','poorer'),('poorer','richer'),('older','younger'),('intelligent','foolish'),('smart','dumb'),('funny','boring'),('powerful','weak'),('interesting','boring'),('crazy','normal'),('real','fake'),('cunning','honest'),('complicated','simple'),('normal','crazy'),('beautiful','ugly'),('clever','dumb')]
lexicons['T4_COUNTRY_CAPITAL'] = [('Afghanistan','Kabul'),('Argentina','Buenos Aires'),('Australia','Canberra'),('Austria','Vienna'),('Azerbaijan','Baku'),('Bangladesh','Dhaka'),('Belarus','Minsk'),('Belgium','Brussels'),('Bhutan','Thimphu'),('Brazil','Brasilia'),('Canada','Ottawa'),('Chile','Santiago'),('China','Beijing'),('Colombia','Bogotá'),('Cuba','Havana'),('Denmark','Copenhagen'),('Ecuador','Quito'),('Egypt','Cairo'),('Fiji','Suva'),('Finland','Helsinki'),('France','Paris'),('Georgia','Tbilisi'),('Germany','Berlin'),('Ghana','Accra'),('Greece','Athens'),('Haiti','Port-au-Prince'),('Hungary','Budapest'),('Iceland','Reykjavik'),('India','New Delhi'),('Indonesia','Jakarta'),('Iran','Tehran'),('Iraq','Baghdad'),('Ireland','Dublin'),('Israel','Jerusalem'),('Italy','Rome'),('Japan','Tokyo'),('Laos','Vientiane'),('Libya','Tripoli'),('Malaysia','Kuala Lumpur'),('Maldives','Male'),('Mexico','Mexico City'),('Nepal','Kathmandu'),('Netherlands','Amsterdam'),('New Zealand','Wellington'),('North Korea','Pyongyang'),('Oman','Muscat'),('Pakistan','Islamabad'),('Philippines','Manila'),('Poland','Warsaw'),('Portugal','Lisbon'),('Qatar','Doha'),('Russia','Moscow'),('Saudi Arabia','Riyadh'),('Singapore','Singapore'),('South Korea','Seoul'),('Sweden','Stockholm'),('Switzerland','Bern'),('Taiwan','Taipei'),('Thailand','Bangkok'),('Turkey','Ankara'),('Ukraine','Kyiv'),('United Arab Emirates','Abu Dhabi'),('United Kingdom','London'),('United States of America','Washington, D.C.'),('Uruguay','Montevideo'),('Vietnam','Hanoi'),('Zimbabwe','Harare')]
lexicons['T5_VV5O'] = [('ask','asks','the question'),('begin','begins','the game'),('call','calls','the number'),('come','comes','home'),('feel','feels','sad'),('find','finds','the key'),('give','gives','the money'),('go','goes','to school'),('hear','hears','the announcement'),('help','helps','the stranger'),('keep','keeps','the change'),('know','knows','the solution'),('leave','leaves','the house'),('like','likes','football'),('live','lives','in a hostel'),('look','looks','distressed'),('make','makes','paintings'),('move','moves','the table'),('play','plays','basketball'),('run','runs','a marathon'),('say','says','the truth'),('see','sees','the clock'),('show','shows','the presentation'),('start','starts','the match'),('talk','talks','nonsense'),('tell','tells','the truth'),('think','thinks','correctly'),('turn','turns','the light'),('use','uses','the money'),('work','works','at office')]
lexicons['T6_CAUSAL'] = [('threw', 'received','the ball'), ('lent','borrowed','the book'), ('spoke about', 'listened about','the environment'), ('bought', 'sold','a phone'), ('taught', 'learnt','history'),('threw', 'received','the bottle'), ('lent','borrowed','the laptop'), ('spoke about', 'listened about','the trip'), ('bought', 'sold','a camera'), ('taught', 'learnt','mathematics')]
lexicons['T7_VERB_TENSE'] = [('met','meet'),('liked','like'),('helped','help'),('ate with','eat with'),('worked with','work with'),('played with','play with'),('danced with','dance with'),('slept with','sleep with'),('criticised','criticise'),('praised','praise'),('called out','call out'),('invited','invite'),('fired','fire'),('hired','hire'),('married','marry')]
lexicons['T8_VERB_ASPECT'] = [('smoking','smoke'),('procrastinating','procrastinate'),('drinking','drink'),('exercising','exercise'),('singing','sing'),('studying','study'),('writing','write'),('playing','play'),('bunking','bunk'),('shouting','shout'),('abusing','abuse')]
lexicons['T9_VERB_WITH_OBJECT'] = [('go to college','going to college','went to college'),('shift to Europe','shifting to Europe','shifted to Europe'),('shift to China','shifting to China','shifted to China'),('shift to Australia','shifting to Australia','shifted to Australia'),('get a divorce','getting a divorce','got a divorce'),('get into a relationship','getting into the relationship','got into a relationship'),('quit the job','quitting the job','quit the job'),('buy a house','buying a house','bought a house'),('sell a house','selling a house','sold a house'),('get married','getting married','got married'),('buy the phone','buying the phone','bought a phone'),('buy a laptop','buying a laptop','bought a laptop'),('waste time', 'wasting time','wasted time'),('fail the exam','failing the exam','failed the exam'),('win the race', 'winning the race','won the race'),('get the scholarship', 'getting the scholarship','got the scholarship')]
lexicons['T10_PROFESSION_ACTION'] = [('writer','write a bestseller'),('writer','write a non-fiction'),('writer','write a self-help book'),('painter','sketch portraits'),('painter','do a digital art'),('painter','paint monuments'),('poet','write on nature'),('poet','write short poems'),('poet','write poems about loss'),('entrepreneur','start a technology company'),('entrepreneur','run a consulting firm'),('entrepreneur','run a trading firm'),('businessman','negotiate better deals'),('businessman','own a conglomerate'),('businessman','work in health sector'),('banker','own a large house'),('banker','manage a portfolio'),('dancer','be a contemporary dancer'),('dancer','be a hip hop dancer'),('dancer','be a folk dance'),('engineer','be a mechanical engineer'),('engineer','be an electrical engineer'),('engineer','work on constructing bridges'),('doctor','cure cancer'),('doctor','be a dentist'),('doctor','be a heart doctor'),('lawyer','be a corporate lawyer'),('lawyer','work on taxation'),('lawyer','work in Supreme Court'),('teacher','teach high school students'),('teacher','teach middle school students'),('teacher','teach geography'),('professor','teach at Harvard'),('professor','teach Psychology'),('professor','teach History'),('professor','teach Mathematics'),('actor','work on Broadway'),('actor','work in TV series'),('actor','work in action films'),('actor','work in romantic movies'),('singer','sing like Adele'),('singer','sing country songs'),('singer','sing in an Opera'),('politician','pass the environment bill'),('politician','work for upliftment of the poor'),('politician','approve the construction of the new bridge'),('accountant','manage balancesheet of companies'),('accountant','manage balancesheet of individuals')]
lexicons['T11_IMPLICATURE'] = [('sat in a car','car'),('sat on a bike','bike'),('sat on a cycle','cycle'),('walked in a house','house'),('walked out of a house','house'),('waited outside a house','house'),('waited outside a car','car'),('picked up a phone','phone'),('picked up a laptop','laptop'),('picked up a wallet','wallet'),('picked up a purse','purse')]
lexicons['T12_RELATIONAL'] = [('brother','sibling','man','father'),('brother','sibling','man','mother'),('brother','sibling','man','son'),('brother','sibling','man','daughter'),('brother','sibling','man','husband'),('brother','sibling','man','wife'),('sister','sibling','woman','father'),('sister','sibling','woman','mother'),('sister','sibling','woman','son'),('sister','sibling','woman','daughter'),('sister','sibling','woman','husband'),('sister','sibling','woman','wife'),('father','child','man','grandfather'),('father','child','man','sister'),('father','child','man','brother'),('father','child','man','mother'),('father','child','man','husband'),('father','child','man','wife'),('mother','child','woman','grandmother'),('mother','child','woman','sister'),('mother','child','woman','brother'),('mother','child','woman','father'),('mother','child','woman','husband'),('mother','child','woman','wife'),('wife','spouse','woman','mother'),('wife','spouse','woman','daughter'),('wife','spouse','woman','father'),('wife','spouse','woman','son'),('wife','spouse','woman','brother'),('wife','spouse','woman','sister'),('husband','spouse','man','mother'),('husband','spouse','man','daughter'),('husband','spouse','man','father'),('husband','spouse','man','son'),('husband','spouse','man','brother'),('husband','spouse','man','sister'),('son','parent','man','brother'),('son','parent','man','sister'),('son','parent','man','mother'),('son','parent','man','father'),('son','parent','man','husband'),('son','parent','man','wife'),('daughter','parent','woman','brother'),('daughter','parent','woman','sister'),('daughter','parent','woman','mother'),('daughter','parent','woman','father'),('daughter','parent','woman','husband'),('daughter','parent','woman','wife')]
lexicons['T13_TAXONOMIC'] = [('colors','red','are available'),('colors','green','are available'),('colors','yellow','are available'),('colors','blue','are available'),('colors','magenta','are available'),('colors','purple','are available'),('colors','crimson','are available'),('colors','white','are available'),('colors','pink','are available'),('colors','black','are available'),('colors','grey','are available'),('cars','BMW','are costly'),('cars','Ferrari','are costly'),('cars','Benz','are costly'),('cars','Toyota','are costly'),('cars','Rolls Royce','are costly'),('cars','Fiat','are costly'),('cars','Renault','are costly'),('fruits','banana','are healthy'),('fruits','apple','are healthy'),('fruits','cherry','are healthy'),('fruits','strawberry','are healthy'),('fruits','peach','are healthy'),('fruits','mango','are healthy'),('mammals','elephant','give birth to young ones'),('mammals','kangaroo','give birth to young ones'),('mammals','cow','give birth to young ones'),('mammals','bat','give birth to young ones'),('mammals','rat','give birth to young ones'),('mammals','rabbit','give birth to young ones'),('mammals','dolphin','give birth to young ones')]

lexicons['COUNTRY'] = [i for i,j in lexicons['T4_COUNTRY_CAPITAL']]
lexicons['VERB'] = [i for i,j,k in lexicons['T5_VV5O']]