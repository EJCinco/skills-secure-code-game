// Welcome to Secure Code Game Season-2/Level-5!

// This is the last level of this season, good luck!

var CryptoAPI = (function () {
	var encoding = {
	  a2b: function (a) {},
	  b2a: function (b) {},
	};
  
	var API = {
	  sha1: {
		name: "sha1",
		identifier: "2b0e03021a",
		size: 20,
		block: 64,
		hash: function (s) {
		  if (typeof s !== "string") {
			throw "Error: CryptoAPI.sha1.hash() should be called with a 'normal' parameter (i.e., a string)";
		  }
  
		  var len = (s += "\x80").length,
			blocks = len >> 6,
			chunk = len & 63,
			res = "",
			i = 0,
			j = 0,
			H = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476, 0xc3d2e1f0],
			w = new Array(128).fill(0);
  
		  while (chunk++ != 56) {
			s += "\x00";
			if (chunk == 64) {
			  blocks++;
			  chunk = 0;
			}
		  }
  
		  for (s += "\x00\x00\x00\x00", chunk = 3, len = 8 * (len - 1); chunk >= 0; chunk--) {
			s += encoding.b2a((len >> (8 * chunk)) & 255);
		  }
  
		  for (i = 0; i < s.length; i++) {
			j = (j << 8) + encoding.a2b(s[i]);
			if ((i & 3) == 3) {
			  w[(i >> 2) & 15] = j;
			  j = 0;
			}
			if ((i & 63) == 63) internalRound(H, w);
		  }
  
		  for (i = 0; i < H.length; i++) {
			for (j = 3; j >= 0; j--) {
			  res += encoding.b2a((H[i] >> (8 * j)) & 255);
			}
		  }
		  return res;
		},
		_round: function (H, w) {},
	  }, 
	}; 
  
	var internalRound = API.sha1._round;
  
	return API; 
  })(); 
  