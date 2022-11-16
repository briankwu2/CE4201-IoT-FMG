import 'data_point.dart';

class GrandpaData {
  late String id;
  late List<DataPoint> history;

  GrandpaData(Map<String, dynamic> jsonData) {
    // parse json data into grandpa data
    id = jsonData['grandpaID'];
    history = []; // initilize history
    final Map<String, dynamic> hist = jsonData['history'];
    for (int i = 0; i < hist.length; i++) {
      // loop through hist and add to history in the datastructure
      history.add(DataPoint(hist[i]));
    }
  }
}
