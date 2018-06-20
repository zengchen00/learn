
if (typeof web3 !== 'undefined') {
        web3 = new Web3(web3.currentProvider);
} else {
        // set the provider you want from Web3.providers
       web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:7545"));
}

// creation of contract object
var MyContract = web3.eth.contract(lisaoAbi);

// initiate contract for an address
var lisaoToken = MyContract.at('0xcfd6bb08b6a7b641a4823ffd5f77ab7e86e523e7');
lisaoToken.totalSupply(function(error, result){
    if(!error){
            console.log(result);
    }
    else
        console.error(error);
});

console.log(lisaoToken.name())

lisaoToken.balanceOf('0x5e03c1B23c51bD1C12AA839a16A51174D749E761',function(error, result){
    if(!error){
            console.log(result.c[0]);
    }
    else
        console.error(error);
});
