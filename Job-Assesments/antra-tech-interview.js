const object = {
    id: 1,
    name: 'David Dong',
    links: [
        { name: 'linkedin',     link: 'linkedin.com'    },
        { name: 'tesla',        link: 'tesla.com'       },
        { name: 'instagram',    link: 'instagram.com'   },
        { name: 'whatsapp',     link: 'whatsapp.com'    },
        { name: 'weibo',        link: 'weibo.com'       },
        { name: 'facebook',     link: 'facebook.com'    },
        { name: 'wechat',       link: 'wechat.com'      },
        { name: 'apple',        link: 'apple.com'       },
        { name: 'cnn',          link: 'cnn.com'         },
        { name: 'fox',          link: 'fox.com'         },
        { name: 'hbo',          link: 'hbo.com'         },
    ]
}

console.log(object.links.find(element => element.name === 'apple').link); 


// apple.com

// const arr = [1, 2, 3, 4];
// for (let i = 0; i < arr.length; i++) {
//   console.log(arr[i]);
// }

// obj.links
// //check to see if apple is the name


// name('apple');

// // // name === 'apple' {
// //   return link
// //   }

// // return the value in link

// loop // 


// indexOf

// // function getLink(obj){

// // }
