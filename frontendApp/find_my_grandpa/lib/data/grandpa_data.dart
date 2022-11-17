import 'data_point.dart';
import 'dart:convert' as convert;

class GrandpaData {
  late String id;
  late List<DataPoint> history;
  GrandpaData() {
    // empty grandpa
    id = "";
    history = [];
  }
  GrandpaData.withJson(String jsonStr) {
    // parse json data into grandpa data
    var jsonData = convert.jsonDecode(jsonStr) as Map<String, dynamic>;
    print(jsonData);
    id = jsonData['grandpaID'];
    print(id);
    history = []; // initilize history
    final List<dynamic> hist = jsonData['history'];
    for (int i = 0; i < hist.length; i++) {
      // loop through hist and add to history in the datastructure
      history.add(DataPoint(hist[i]));
    }
  }
}
