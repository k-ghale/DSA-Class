function TOH(n, source, aux, dest) {
  if (n == 1) {
    console.log(`Moving disk ${n} from ${source} to ${dest}`);
    return;
  }

  TOH(n - 1, source, dest, aux);
  console.log(`Moving disk ${n} from ${source} to ${dest}`);
  TOH(n - 1, aux, source, dest);
}
TOH(3, "a", "b", "c");
console.log("");

function fact(n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * fact(n - 1);
  }
}
console.log(fact(5));


function fibonacci(n){
    if(n === 0){
        return 0;
    }
    else if(n === 1){
        return 1;
    }
    else{
        return fibonacci(n-1) + fibonacci(n-2);
    }
}
console.log(fibonacci(6));