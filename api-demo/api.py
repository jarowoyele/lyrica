from flask import Flask, request,jsonify
from flask_restful import reqparse
from flask_cors import CORS
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from split import unique



app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def index():
    return "<h1>Joy Arowoyele Python Demo</h1><p>This site is a demo API for Arowoyele Joy's project.</p>"

# @app.route('/lyricsfilter', methods=['GET'])
# def filter_lyrics():
#     lyrics = "Woo, woo I pull up like How you pull up, Baby? How you pull up? (Oh, oh, oh) How you pull up? I pull up (woo, Seth in the kitchen) Let's go Brand new Lamborghini, fuck a cop car With the pistol on my hip like I'm a cop (yeah, yeah, yeah) Have you ever met a real nigga rockstar? This ain't no guitar, bitch, this a Glock (woo) My Glock told me to promise you gon' squeeze me (woo) You better let me go the day you need me (woo) Soon as you up me on that nigga, get to bustin' (woo) And if I ain't enough, go get the chop It's safe to say I earned it Ain't a nigga gave me nothin' (yeah, yeah, yeah) I'm ready to hop out on a nigga, get to bustin' Know you heard me say, \"You play, you lay\" Don't make me push the button Full of pain, dropped enough tears to fill up a fuckin' bucket Goin' for buckets, I bought a chopper I got a big drum, it hold a 100, ain't goin' for nothin' I'm ready to air it out on all these niggas, I can see 'em runnin' Just talked to my mama She hit me on FaceTime just to check up on me and my brother I'm really the baby, she know that her youngest son Was always guaranteed to get the money (okay, let's go) She know that her baby boy was always guaranteed to get the loot She know what I do, she know 'fore I run from a nigga I'ma pull it out and shoot (boom) PTSD, I'm always waking up in cold sweats like I got the flu My daughter a G She saw me kill a nigga in front of her before the age of two And I'll kill another nigga too 'Fore I let another nigga do somethin' to you Long as you know that, don't let nobody tell you different Daddy love you (yeah, yeah) Let's go Brand new Lamborghini, fuck a cop car With the pistol on my hip like I'm a cop (yeah, yeah, yeah) Have you ever met a real nigga rockstar? This ain't no guitar, bitch, this a Glock (woo) My Glock told me to promise you gon' squeeze me (woo) You better let me go the day you need me (woo) Soon as you up me on that nigga, get to bustin' (yeah) And if I ain't enough, go get the chop (yeah, yeah) Keep a Glocky when I ride in the Suburban 'Cause the codeine had a young nigga swervin' I got the mop, watch me wash 'em like detergent And I'm ballin', that's why it's diamonds on my jersey Slide on opps' side and flip the block back, yeah, yeah My junior popped him and left him lopsided, yeah, yeah We spin his block, got the rebound, Dennis Rodman You fool me one time, you can't cross me again 1200 horsepower, I get lost in the wind If he talkin' on the yard, the pen' dogs'll take his chin Maybach SUV for my refugees Buy blocks in the hood, put money in the streets I was solo when the opps caught me at the gas station Had it on me, 30 thousand, thought it was my last day But they ain't even want no smoke If I had to choose it, murder what she wrote Let's go Brand new Lamborghini, fuck a cop car With the pistol on my hip like I'm a cop (yeah, yeah, yeah) Have you ever met a real nigga rockstar? This ain't no guitar, bitch, this a Glock (woo) My Glock told me to promise you gon' squeeze me (woo) You better let me go the day you need me (woo) Soon as you up me on that nigga, get to bustin' (woo) And if I ain't enough, go get the chop"
#     return jsonify(parse_lyrics(lyrics))

@app.route('/lyricsfilter', methods=['POST'])
def filter_lyrics():
    parser = reqparse.RequestParser()
    parser.add_argument('lyrics',required=True)
    args = parser.parse_args()

    #request_data = request.json
    #lyrics = request_data["lyrics"]
    lyrics = args['lyrics']
    return jsonify(parse_lyrics(lyrics))

def parse_lyrics(lyrics):
    profane_words = "4r5e5h1t,fuck,bustin\',busting,fucked,5hit,a55,anal,anus,ar5e,arrse,arse,ass,ass-fucker,asses,assfucker,assfukka,asshole,assholes,asswhole,a_s_s,b!tch,b00bs,b17ch,b1tch,ballbag,balls,ballsack,bastard,beastial,beastiality,bellend,bestial,bestiality,bi+ch,biatch,bitch,bitcher,bitchers,bitches,bitchin,bitching,bloody,blow job,blowjob,blowjobs,boiolas,bollock,bollok,boner,boob,boobs,booobs,boooobs,booooobs,booooooobs,breasts,buceta,bugger,bum,bunny fucker,butt,butthole,buttmuch,buttplug,c0ck,c0cksucker,carpet muncher,cawk,chinkcipa,cl1t,clit,clitoris,clits,cnut,cock,cock-sucker,cockface,cockhead,cockmunch,cockmuncher,cocks,cocksuck, cocksucked, cocksucker,cocksucking,cocksucks,cocksuka,cocksukka,cok,cokmuncher,coksucka,coon,cox,crap,cum,cummer,cumming,cums,cumshot,cunilingus,cunillingus,cunnilingus,cunt,cuntlick, cuntlicker, cuntlicking, cunts,cyalis,cyberfuc,cyberfuck, cyberfucked, cyberfucker,cyberfuckerscyberfucking,d1ck,damn,dick,dickhead,dildo,dildos,dink,dinks,dirsa,dlck,dog-fucker,doggin,dogging,donkeyribber,doosh,duche,dyke,ejaculate,ejaculated,ejaculates,ejaculating, ejaculatings,ejaculation,ejakulate,f u c k,f u c k e r,f4nny,fag,fagging,faggitt,faggot,faggs,fagot,fagots,fags,fanny,fannyflaps,fannyfucker,fanyy,fatass,fcuk,fcuker,fcuking,feck,fecker,felching,fellate,fellatio,fingerfuck, fingerfucked, fingerfucker,fingerfuckers,fingerfucking,fingerfucks,fistfuck,fistfucked, fistfucker,fistfuckers, fistfucking, fistfuckings, fistfucks, flangefook,fookefuck,fucka,fucked,fucker,fuckers,fuckhead,fuckheads,fuckin,fucking,fuckings,fuckingshitmotherfucker,fuckme, fucks,fuckwhit,fuckwit,fudge packer,fudgepacker,fuk,fukerfukker,fukkin,fuks,fukwhit,fukwit,fux,fux0r,f_u_c_k,gangbang,gangbanged, gangbangs, gaylord,gaysex,goatse,God,god-dam,god-damned,goddamn,goddamned,hardcoresex, hell,heshe,hoar,hoare,hoer,homo,hore,horniest,horny,hotsex,jack-off, jackoff,jap,jerk-off, jism,jiz,jizm, jizz,kawk,knob,knobeadknobed,knobend,knobhead,knobjocky,knobjokey,kock,kondum,kondums,kum,kummer,kumming,kums,kunilingus,l3i+ch,l3itch,labia,lmfao,lust,lusting,m0f0,m0fo,m45terbate,ma5terb8,ma5terbate,masochist,master-bate,masterb8,masterbat*,masterbat3,masterbate,masterbation,masterbations,masturbate,mo-fo,mof0,mofo,mothafuck,mothafucka,mothafuckas,mothafuckaz,mothafucked, mothafucker,mothafuckers,mothafuckin,mothafucking, mothafuckings,mothafucks,mother fucker,motherfuck,motherfucked,motherfucker,motherfuckers,motherfuckin,motherfucking,motherfuckings,motherfuckka,motherfucks,muff,mutha,muthafecker,muthafuckker,muther,mutherfucker,n1gga,n1gger,nazi,nigg3r,nigg4h,nigga,niggah,niggas,niggaz,nigger,niggers, nob,nob jokey,nobhead,nobjocky,nobjokey,numbnuts,nutsack,orgasim,orgasims, orgasm,orgasms, p0rn,pawn,pecker,penis,penisfucker,phonesex,phuck,phuk,phuked,phuking,phukked,phukking,phuks,phuq,pigfucker,pimpis,piss,pissed,pisser,pissers,pisses,pissflaps,pissin, pissing,pissoff,poop,porn,porno,pornography,pornos,prick,pricks, pron,pube,pusse,pussi,pussies,pussy,pussys, rectum,retard,rimjaw,rimming,s hit,s.o.b.,sadist,schlong,screwing,scroat,scrote,scrotum,semen,sex,sh!+,sh!t,sh1tshag,shagger,shaggin,shagging,shemale,shi+,shit,shitdick,shite,shited,shitey,shitfuck,shitfull,shithead,shiting,shitings,shits,shitted,shitter,shitters, shitting,shittings,shitty,skank,slut,sluts,smegma,smut,snatch,son-of-a-bitch,spac,spunk,s_h_i_t,t1tt1e5,t1tties,teets,teez,testical,testicle,tit,titfuck,tits,titt,tittie5,tittiefucker,titties,tittyfuck,tittywank,titwank,tosser,turd,tw4t,twat,twathead,twatty,twunt,twunter,v14gra,v1gra,vagina,viagra,vulva,w00se,wang,wank,wanker,wanky,whoar,whore,willies,willy,xrated,xxx"
    profane = profane_words.replace(",", " ")
    profane = profane.split(" ")
    profane = unique.union(set(profane))
    stpwrds = stopwords.words("english")
    tokens = word_tokenize(lyrics)
    removing_stopwords = [words for words in tokens if not words in stpwrds]
    new_stopwords = stopwords.words("english")
    new_stopwords = new_stopwords.extend(profane)
    removing = [word for word in removing_stopwords if word in profane]
    return removing

app.run(debug=True)