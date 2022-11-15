import 'dart:io';

import 'package:http/http.dart' as http;
import 'dart:convert' as convert;

class NetowrkManager {
  static final NetowrkManager _netowrkManager = NetowrkManager._internal();
  static final String fmgURL = '127.0.0.1:5000';

  factory NetowrkManager() {
    return _netowrkManager;
  }

  NetowrkManager._internal();

  void login(String username) async {
    // gets grandpa from database and

    // get grandpa and save it
    Map<String, String> parmsReq = {'grandpaID': username};
    print("Creating url");
    //var parsedURL = Uri.parse(fmgURL);
    //print(parsedURL);

    var url = Uri.http(fmgURL, "/grandpa_data/", parmsReq);
    // var url = Uri.parse('http://127.0.0.1:5000/');
    print(url);
    try {
      var response = await http.get(url);
      print(response.statusCode);
      var jsonDecoded = convert.jsonDecode(response.body);
      print(jsonDecoded);
    } catch (e) {
      print(e);
    }
    // var response = await http.get(url);
    // print(response);
    // if (response.statusCode == 200) {
    //   // print(response.statusCode);
    //   print("response successful");
    //   // var jsonResponse = convert.jsonDecode(response.body) as Map<String, dynamic>;
    //   // print(jsonResponse.toString());
    // } else {
    //   print('Request failed with status: ${response.statusCode}.');
    // }
  }
}
