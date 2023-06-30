const { ethers } = require("ethers");
const axios = require('axios');


async function get_ethscript(start_index,times){
  let script_list = []
  for(let i = 0;i < times ;i++){

      let text = `data:,{"p":"nrc-20","op":"mint","tick":"bnbs","id":"${start_index + i}","amt":"1000"}`
      script_list.push(text)
  }
  console.log(script_list);
  return script_list;
}
async function send(wallet,provider,inputdata,nonce){
    try {
        const recipientAddress = wallet.address;
        console.log(`recipientAddress: ${recipientAddress}`);
        let transaction = {
            from: await ethers.utils.getAddress(wallet.address),
            to: await ethers.utils.getAddress(recipientAddress),
            value: 0,
            nonce:nonce
        };
        let gas = await provider.estimateGas(transaction);
        transaction.gasLimit = parseInt(gas.toString()) + 21000;
        let gasp =  await provider.getGasPrice();
        transaction.gasPrice = parseInt(gasp.toString());
        transaction.data = await ethers.utils.hexlify(ethers.utils.toUtf8Bytes(inputdata));
        // 发送交易
        let tx = await wallet.sendTransaction(transaction);
        console.log(`Transaction hash: ${tx.hash}`);

    } catch (err) {
        console.error(err);
    }
}
async function main(start=1000,times=20,rpc,privateKey){

 
  //手动指定起始位置和数量
  let script_list = await get_ethscript(start,times);
  //let script_list = await get_distance();
  //设置rpc连接
  const provider = await new ethers.providers.JsonRpcProvider(rpc);
  console.log(`${await provider.getBlockNumber()}`)
  const wallet =await new ethers.Wallet(privateKey, provider);
  let nonce = await provider.getTransactionCount(wallet.address, 'latest');
    for(let i = 0;i<times;i++){
        try{
            
            console.log(`${i},${script_list[i]}`);
            await send(wallet,provider,script_list[i],nonce);
            nonce += 1;
        }catch(error){
            console.error(error);
        }
    }
    console.log("结束");

}
/**
 * start 起始位置
 * times 数量 递增
 * rpc rpc地址
 * privateKey 私钥
 * 修改 text 铭文格式
 */
main(start=1000,times=10,rpc=`https://polygon-mumbai.blockpi.network/v1/rpc/public`,privateKey=`填写私钥`)

const { ethers } = require("ethers");
const axios = require('axios');


async function get_ethscript(start_index,times){
  let script_list = []
  for(let i = 0;i < times ;i++){

      let text = `data:,{"p":"nrc-20","op":"mint","tick":"bnbs","id":"${start_index + i}","amt":"1000"}`
      script_list.push(text)
  }
  console.log(script_list);
  return script_list;
}
async function send(wallet,provider,inputdata,nonce){
    try {
        const recipientAddress = wallet.address;
        console.log(`recipientAddress: ${recipientAddress}`);
        let transaction = {
            from: await ethers.utils.getAddress(wallet.address),
            to: await ethers.utils.getAddress(recipientAddress),
            value: 0,
            nonce:nonce
        };
        let gas = await provider.estimateGas(transaction);
        transaction.gasLimit = parseInt(gas.toString()) + 21000;
        let gasp =  await provider.getGasPrice();
        transaction.gasPrice = parseInt(gasp.toString());
        transaction.data = await ethers.utils.hexlify(ethers.utils.toUtf8Bytes(inputdata));
        // 发送交易
        let tx = await wallet.sendTransaction(transaction);
        console.log(`Transaction hash: ${tx.hash}`);

    } catch (err) {
        console.error(err);
    }
}
async function main(start=1000,times=20,rpc,privateKey){

 
    //手动指定起始位置和数量
    let script_list = await get_ethscript(start,times);
    //let script_list = await get_distance();
    //设置rpc连接
    const provider = await new ethers.providers.JsonRpcProvider(rpc);
    console.log(`${await provider.getBlockNumber()}`)
    const wallet =await new ethers.Wallet(privateKey, provider);
    let nonce = await provider.getTransactionCount(wallet.address, 'latest');
    let index = 0;
    let intervalId = setInterval(async function() {
        try{
            if(index<times){
                console.log(`${index},${script_list[index]}`);
                await send(wallet,provider,script_list[index],nonce+index);
                index += 1;
            }else{
                clearInterval(intervalId);
            }
        
        }catch(error){
        console.error(error);
        }
    //无视线程阻塞 2.5s发送一个交易
    },  2500 );

    console.log("结束");

}
/**
 * start 起始位置
 * times 数量 递增
 * rpc rpc地址
 * privateKey 私钥
 * 修改 text 铭文格式
 */
main(start=1000,times=10,rpc=`https://polygon-mumbai.blockpi.network/v1/rpc/public`,privateKey=`填写私钥`)

