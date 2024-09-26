import nltk
import re
from collections import Counter
from wordfreq import zipf_frequency
from nltk.corpus import words
from statistics import mean, median

PREVIOUS_ANSWERS = [
    word.lower()
    for word in "ARISE ABASE ABATE ABBEY ABYSS ACUTE ADOBE AGAPE AGATE AGREE AHEAD ALBUM ALIEN ALLOW ALOFT ALONE "
    "ALPHA ALTAR AMPLE ANGRY APHID APRON ARGUE AROMA ASIDE ASKEW ASSET ATOLL ATONE AUDIT AWAKE AWFUL "
    "BADGE BADLY BANAL BASIC BATON BATTY BAYOU BEADY BEING BELCH BELLY BENCH BERTH BIOME BLACK BLAND "
    "BLEED BLOKE BLOWN BLUFF BLURT BLUSH BOOBY BOOST BOOZE BOOZY BRAKE BREAK BRIAR BRIBE BRINE BRING "
    "BRINK BUGGY CACAO CANNY CARGO CATER CAULK CHAMP CHANT CHARM CHEAT CHEEK CHIEF CHEST CHILL CHOKE "
    "CHUNK CHUTE CIGAR CINCH CIVIC CLASS CLICK CLING CLOCK CLOTH CLOWN CLUCK COAST COLON COMET COMMA "
    "CONIC CORNY COULD COYLY CRAMP CRANK CRASS CRATE CRAZE CRAZY CREAK CREPT CRIMP CROAK CRUST CYNIC "
    "DEATH DELTA DELVE DEPOT DEPTH DIGIT DODGE DONOR DOUBT DOWRY DOZEN DRAIN DRINK DROLL DUCHY DUTCH "
    "DWARF EGRET ELDER ELOPE ENEMA EPOCH EPOXY ERODE ERROR ESSAY EVADE EXULT FARCE FAVOR FEIGN FERRY "
    "FEWER FIELD FINER FIRST FIXER FJORD FLAIR FLESH FLICK FLING FLOAT FLOCK FLOOD FLOSS FLUFF FLUME "
    "FOCAL FOCUS FORAY FORGE FORGO FORTH FOUND FOYER FRAME FRESH FRONT FROTH FUNGI GAMER GAMMA GAUDY "
    "GAUZE GAWKY GECKO GIRTH GLASS GLEAN GLOAT GLOOM GOLEM GONER GOOSE GORGE GOUGE GRADE GREAT GREET "
    "GRIME GRIPE GROIN GROUP GROWL GRUEL GUILD GULLY HAIRY HATCH HEATH HEIST HELIX HERON HINGE HOARD "
    "HOMER HUMOR HUMPH HUNKY HUTCH HYPER INERT INPUT INTER IRONY ISLET IVORY JAUNT KARMA KEBAB KHAKI "
    "KNOLL LABEL LABOR LAPEL LAPSE LARVA LEERY LIGHT LILAC LINEN LIVER LOFTY LOOPY LOSER LOWLY LUSTY "
    "LYING MADAM MAJOR MANOR MARRY MASSE MAXIM MERIT METAL MIDGE MIDST MIMIC MINCE MODEL MOIST MONEY "
    "MONTH MOTOR MOTTO MOULT MOUNT MOURN MOVIE NASTY NATAL NAVAL NEEDY NIGHT NYMPH OFFAL OLIVE OTHER "
    "OUGHT OUTDO OXIDE PANEL PANIC PAPER PARER PARRY PATTY PAUSE PEACH PERCH PERKY PHASE PICKY PIETY "
    "PILOT PINTO PITHY PLANT PLEAT PLUCK POINT POKER POUND POWER PRICK PRIDE PRIMO PRINT PRIZE PROVE "
    "PROXY PULPY PURGE QUART QUERY QUIET RADIO REACT REBUS REBUT RENEW REPAY RETCH RETRO RHINO RHYME "
    "ROBIN ROBOT ROGUE ROOMY ROUGE ROUND ROYAL RUDER RUPEE RUSTY SALAD SAUTE SCARE SCOUR SCRAP SEEDY "
    "SERVE SEVER SHAKE SHALL SHAME SHARD SHAWL SHINE SHIRE SHOWN SHOWY SHRUB SHRUG SIEGE SISSY SKILL "
    "SLOSH SLUMP SLUNG SMART SMEAR SMELT SMITE SNOUT SOLAR SOLVE SONIC SOWER SPEND SPICY SPIKE SPILL "
    "SPRAY SQUAD STAFF STAIR STAND START STEAD STEED STICK STINK STOMP STOOL STORE STORY STOUT STOVE "
    "SUGAR SURER SWEET SWILL SWIRL TACIT TANGY TAPIR TAUNT TEASE THEIR THEME THORN THOSE THUMB THYME "
    "TIARA TIBIA TIGER TILDE TIPSY TODAY TOTEM TRACE TRAIN TRAIT TRASH TRAWL TREAT TRIAD TRITE TROLL "
    "TROPE TROVE TRUSS TRYST TWANG TWEED TWICE ULCER ULTRA UNFED UNFIT UNIFY UNMET UPSET USHER USING "
    "VIRAL VITAL VIVID VODKA VOICE VOUCH WACKY WASTE WATCH WEARY WEDGE WHACK WHELP WHOOP WINCE WOOER "
    "WORLD WOVEN WROTE WRUNG YEARN YIELD YOUTH ZESTY ALIKE RECAP".split(" ")
]


def get_words_of_length_n(n):
    w = filter(lambda w: len(w) == n, words.words())
    return list(set([word.lower() for word in w]))


def get_letters_by_appearance_in_words(word_list):
    set_letters = "".join([l for word in word_list for l in set(word)])
    return [l[0] for l in Counter(set_letters).most_common(26)]


def get_words_comprised_of_letters(letters, word_list, word_len=5):
    ls = "".join(letters)

    def check_consists_of_unique_letters(word):
        return (
            re.search(rf"[{ls}]{{{word_len}}}", word) is not None
            and len(set(word)) == word_len
        )

    return list(filter(lambda w: check_consists_of_unique_letters(w), word_list))


def get_partial_wordle_solutions(partial: str, excluded="", included=""):
    # Get 5 letter words that have included letters, don't have excluded, and are not previous answers
    def filter_by_included(word):
        return (
            not bool(
                [
                    letter
                    for letter in excluded
                    if letter in word and letter not in partial
                ]
            )
            and all([letter in word for letter in included])
            and word not in PREVIOUS_ANSWERS
        )

    # Parse all five letter words
    five_letter_words = (
        list(filter(filter_by_included, get_words_of_length_n(5)))
        if included or excluded
        else get_words_of_length_n(5)
    )

    # calculate the median frequency of past solutions
    med_freq = median([zipf_frequency(word, "en") for word in PREVIOUS_ANSWERS])

    def score_word_by_commonality(word):
        return abs(med_freq - zipf_frequency(word, "en"))

    # Turn partial word asterisks into alphabetic characters and encode as a raw string.
    non_letters = r"\d"
    r = (
        partial.replace(
            "*", f"(?:(?!{excluded if len(excluded) else non_letters})[a-z])"
        )
        .encode("unicode-escape")
        .decode()
    )
    # make sure letters that have previously been guessed

    # Sort by closeness to mean word frequency, excluding rare words and words with excluded characters
    return sorted(
        [
            word
            for word in five_letter_words
            if (re.search(r, word) is not None) and zipf_frequency(word, "en") > 0
        ],
        key=lambda w: score_word_by_commonality(w),
    )


print(get_partial_wordle_solutions("w****"))
