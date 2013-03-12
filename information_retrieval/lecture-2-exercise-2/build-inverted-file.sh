# Part I a)

function a {
    mkdir tmp

    for file in corpus/*
    do
        echo "Processing " $file
        tr ' ' '\n' < $file > tmp/$(basename $file)
    done
}

# Part I b)

function b {
    mkdir tmp2

    cat /dev/null > tmp2/terms
    cat tmp/* > tmp2/terms
    sort tmp2/terms > tmp2/sorted-terms
    uniq -c tmp2/sorted-terms > tmp2/counted-sorted-terms

    head tmp2/counted-sorted-items
}

# Part I c)

function c {
    mkdir tmp
    rm tmp/*

    # for file in corpus/*
    for file in corpus/XIE20000817.0173
    do
        echo "Splitting " $file
        tr ' ' '\n' < $file > tmp/$(basename $file)
    done

    mkdir tmp2
    rm tmp2/*

    cat /dev/null > tmp2/terms
    for file in tmp/*
    do
        for line in $(cat $file)
        do
            echo $(basename $file) $line
        done
    done > tmp2/terms
    sort tmp2/terms > tmp2/sorted-terms
    uniq -c tmp2/sorted-terms > tmp2/counted-sorted-terms

    head tmp2/counted-sorted-terms
    echo
    tail tmp2/counted-sorted-terms
}

# Part I d)

function d {
    mkdir tmp
    rm tmp/*

    # for file in corpus/*
    for file in corpus/XIE20000817.0173
    do
        echo "Splitting " $file
        # Tokenise. Remove punctuation immediately following words.
        # s substitute, g global
        cat $file \
        | tr ' ' '\n' \
        | sed 's/[.?!]$//g' \
        > tmp/$(basename $file)
    done

    mkdir tmp2
    rm tmp2/*

    cat /dev/null > tmp2/terms
    for file in tmp/*
    do
        for line in $(cat $file)
        do
            echo $(basename $file) $line
        done
    done > tmp2/terms
    sort tmp2/terms > tmp2/sorted-terms
    uniq -c tmp2/sorted-terms > tmp2/counted-sorted-terms

    head tmp2/counted-sorted-terms
    echo
    tail tmp2/counted-sorted-terms
}

# Part I e)

function e {
    mkdir tmp
    rm tmp/*

    # for file in corpus/*
    for file in corpus/XIE20000817.0173
    do
        echo "Splitting " $file
        # Tokenise. Remove punctuation immediately following words.
        # s substitute, g global
        cat $file \
        | tr ' ' '\n' \
        | sed 's/[.?!]$//g' \
        | tr '[A-Z]' '[a-z]' \
        > tmp/$(basename $file)
    done

    mkdir tmp2
    rm tmp2/*

    cat /dev/null > tmp2/terms
    for file in tmp/*
    do
        for line in $(cat $file)
        do
            echo $(basename $file) $line
        done
    done > tmp2/terms
    sort tmp2/terms > tmp2/sorted-terms
    uniq -c tmp2/sorted-terms > tmp2/counted-sorted-terms

    head tmp2/counted-sorted-terms
    echo
    tail tmp2/counted-sorted-terms
}

e