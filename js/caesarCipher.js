exports.caesarCipher = function(word, shift) {
    let alphaLower=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    let alphaUpper=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    let answer=''
    for (let i=0; i<word.length; i++){
        if(word[i] == word[i].toUpperCase() && /^[A-Z]/.test(word[i])){
            let idx= alphaUpper.indexOf(word[i])+shift;
            if(idx > 26){
                idx -= 26
            }
            else if(idx<0){
                idx+=26
            }
            answer+= alphaUpper[idx]
        }
        else if(word[i]== word[i].toLowerCase() && /^[a-z]/.test(word[i])){
            let idx= alphaLower.indexOf(word[i])+shift
            if(idx>26){
                idx -= 26
            }
            else if(idx<0){
                idx+=26
            }
            answer+= alphaLower[idx]
        }
        else{
            answer+=word[i]
        }
    }
    return answer;
};
