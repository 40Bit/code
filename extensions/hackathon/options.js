  let page = document.getElementById('buttonDiv');
  let timeOne = document.getElementById('timeOne');
  let timeTwo = document.getElementById('timeTwo');
  let timeThree = document.getElementById('timeThree');
  
  const kButtonColors = ['#e8453c', '#ffa126', '#ede500', '#3aa757', '#48b5aa', '#4688f1', '#a30096'];
  function constructOptions(kButtonColors) {
    for (let item of kButtonColors) {
      let button = document.createElement('button');
      button.style.backgroundColor = item;
      button.addEventListener('click', function() {
        chrome.storage.sync.set({color: item}, function() {
          console.log('color is ' + item);
        })
      });
      page.appendChild(button);
    }

	timeOne.onclick = function() {
		var timeOne = prompt('Minutes:')
		chrome.storage.sync.set({timeOne: timeOne})
	}
	
	timeTwo.onclick = function() {
		var timeTwo = prompt('Minutes:')
		chrome.storage.sync.set({timeTwo: timeTwo})
	}
	
	timeThree.onclick = function() {
		var timeThree = prompt('Minutes:')
		chrome.storage.sync.set({timeThree: timeThree})	
	}
	
  }
  constructOptions(kButtonColors);