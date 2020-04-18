let firstButton = document.getElementById('firstButton');
chrome.storage.sync.get('timeOne', function(data){
		if (data.timeOne == undefined) {
    	chrome.storage.sync.set({timeOne: 30});
    	data.timeOne = 30
	}
   firstButton.innerHTML = data.timeOne
})

let secondButton = document.getElementById('secondButton')
chrome.storage.sync.get('timeTwo', function(data){
	if (data.timeTwo == undefined) {	
    	chrome.storage.sync.set({timeTwo: 45})
    	data.timeTwo = 45
    }
   secondButton.innerHTML = data.timeTwo
})

let thirdButton = document.getElementById('thirdButton')
chrome.storage.sync.get('timeThree', function(data){
	if (data.timeThree == undefined) {
    	chrome.storage.sync.set({timeThree: 60})
    	data.timeThree = 60
  	}
   thirdButton.innerHTML = data.timeThree
})

  chrome.storage.sync.get('color', function(data) {
    firstButton.style.backgroundColor = data.color
    firstButton.setAttribute('value', data.color)
  });
  
  secondButton.style.backgroundColor = 'red'
  secondButton.setAttribute('value', 'red')
  
  thirdButton.style.backgroundColor = 'steelblue'
  thirdButton.setAttribute('value', 'steelblue')
  
firstButton.onclick = function() {
	chrome.storage.sync.get('timeOne', function(data){
	timeOne = data.timeOne;
	setTimeout(function(){ 
	  alert("It's time for your class!") 
	}, timeOne * 1000)
});
}

secondButton.onclick = function() {
	chrome.storage.sync.get('timeTwo', function(data){
	timeTwo = data.timeTwo;
	setTimeout(function(){ 
	  alert("It's time for your class!") 
	}, timeTwo * 1000)
});
}

thirdButton.onclick = function() {
	chrome.storage.sync.get('timeThree', function(data){
	let timeThree = data.timeThree;
	setTimeout(function(){ 
	  alert("It's time for your class!") 
	}, timeThree * 1000)
});
}