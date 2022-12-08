import 'package:find_my_grandpa/support_classes/state_manager.dart';
import 'package:flutter/material.dart';
import 'package:flutter/src/foundation/key.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:flutter_map/flutter_map.dart';
import 'package:flutter_map_marker_cluster/flutter_map_marker_cluster.dart';
//import 'package:latlong/latlong.dart';
// import 'package:latlong/latlong.dart';
import 'package:latlong2/latlong.dart';
import 'package:syncfusion_flutter_charts/sparkcharts.dart';

class DashBoardWidget extends StatefulWidget {
  static const String route = "/dashboard";
  const DashBoardWidget({Key? key}) : super(key: key);

  @override
  State<DashBoardWidget> createState() => _DashBoardWidgetState();
}

class _DashBoardWidgetState extends State<DashBoardWidget> {
  MapController _mapController = MapController();
  final PopupController _popupController = PopupController();
  double _zoom = 7;
  List<LatLng> _latLngList = [
    LatLng(13, 77.5),
    LatLng(13.02, 77.51),
    LatLng(13.05, 77.53),
    LatLng(13.055, 77.54),
    LatLng(13.059, 77.55),
    LatLng(13.07, 77.55),
    LatLng(13.1, 77.5342),
    LatLng(13.12, 77.51),
    LatLng(13.015, 77.53),
    LatLng(13.155, 77.54),
    LatLng(13.159, 77.55),
    LatLng(13.17, 77.55),
  ];
  List<LatLng> gPos = [
    LatLng(32.9882741666667, -96.7705133333333),
    LatLng(32.9865563333333, -96.7481523333333),
    LatLng(32.9882056666667, -96.770447),
    LatLng(32.9858723333333, -96.7525996666667)
  ];

  List<Marker> _markers = [];

  @override
  void initState() {
    _markers = StateManager()
        .getGrandpa()
        .history
        .map((point) => Marker(
              point: point.point,
              width: 40,
              height: 40,
              builder: (context) => Icon(
                Icons.circle,
                size: 20,
                color: Colors.red,
              ),
            ))
        .toList();
    super.initState();
  }

  grandpaAlert() async {
    return showDialog(
      context: context,
      barrierDismissible: false,
      builder: (BuildContext context) {
        return AlertDialog(
          title: const Text('Grandpa lost'),
          content: SingleChildScrollView(
            child: ListBody(
              children: const <Widget>[
                Text('Grandpa is lost'),
                Text('Last scene at: '),
              ],
            ),
          ),
          actions: <Widget>[
            TextButton(
              child: const Text('Dissmiss'),
              onPressed: () {
                Navigator.of(context).pop();
              },
            ),
          ],
        );
      },
    );
  }

  Widget triggerAlertGrandpa() {
    return ElevatedButton(
      onPressed: () {
        grandpaAlert();
      },
      child: Text("test grandpa alert"),
    );
  }

  @override
  Widget build(BuildContext context) {
    double width = MediaQuery.of(context).size.width;
    double hegiht = MediaQuery.of(context).size.height;
    return Scaffold(
        appBar: AppBar(
          title: Text('Map'),
        ),
        floatingActionButton: triggerAlertGrandpa(),
        body: Stack(
          children: [
            Positioned.fill(
                top: 20,
                child: Align(
                    alignment: Alignment.topCenter,
                    child:
                        Text("logged in: " + StateManager().getGrandpa().id))),
            Positioned.fill(
                top: 50,
                child: Container(
                    width: 100,
                    height: 100,
                    child: Align(
                        alignment: Alignment.topCenter,
                        child: Container(
                            width: 100,
                            height: 100,
                            child: Image.asset("assets/grandpa.jpg"))))),
            Positioned(
                bottom: 0.3 * hegiht,
                child: Container(
                  width: width,
                  height: 0.5 * hegiht,
                  child: FlutterMap(
                    mapController: _mapController,
                    options: MapOptions(
                      // swPanBoundary: LatLng(13, 77.5),
                      // nePanBoundary: LatLng(13.07001, 77.58),
                      center: StateManager().getGrandpa().firstPoint(),
                      bounds: LatLngBounds.fromPoints(
                          StateManager().getGrandpa().getPosList()),
                      zoom: _zoom,
                      plugins: [
                        MarkerClusterPlugin(),
                      ],
                    ),
                    layers: [
                      TileLayerOptions(
                        minZoom: 2,
                        maxZoom: 18,
                        backgroundColor: Colors.black,
                        // errorImage: ,
                        urlTemplate:
                            'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
                        subdomains: ['a', 'b', 'c'],
                      ),
                      MarkerClusterLayerOptions(
                        maxClusterRadius: 190,
                        disableClusteringAtZoom: 16,
                        size: Size(50, 50),
                        fitBoundsOptions: FitBoundsOptions(
                          padding: EdgeInsets.all(50),
                        ),
                        markers: _markers,
                        polygonOptions: PolygonOptions(
                            borderColor: Colors.blueAccent,
                            color: Colors.black12,
                            borderStrokeWidth: 3),
                        popupOptions: PopupOptions(
                            popupSnap: PopupSnap.mapCenter,
                            popupController: _popupController,
                            popupBuilder: (_, marker) => Align(
                                  alignment: Alignment.topCenter,
                                  child: Container(
                                      width: 1000,
                                      height: 20,
                                      color: Colors.amberAccent,
                                      child: Text(
                                          'Grandpa position at: 9:00 AM' +
                                              marker.point.toString())),
                                )),
                        builder: (context, markers) {
                          return Container(
                            alignment: Alignment.center,
                            decoration: BoxDecoration(
                                color: Colors.orange, shape: BoxShape.circle),
                            child: Text('${markers.length}'),
                          );
                        },
                      ),
                    ],
                  ),
                )),
            Positioned(
                bottom: 0,
                child: SfSparkLineChart(
                  trackball: SparkChartTrackball(
                      activationMode: SparkChartActivationMode.tap),
                  //Enable marker
                  marker: SparkChartMarker(
                      displayMode: SparkChartMarkerDisplayMode.all),
                  //Enable data label
                  labelDisplayMode: SparkChartLabelDisplayMode.all,
                  data: StateManager().getGrandpa().getBPM(),
                ))
          ],
        ));
  }
  // @override
  // Widget build(BuildContext context) {
  //   return Scaffold(
  //       // appBar: AppBar(
  //       //   title: Text("Dashboard"),
  //       // ),
  //       body: Center(
  //           child: Column(
  //     children: [
  //       Text("Logged in " + StateManager().getGrandpa().id.toString()),
  //       Container(
  //           width: 200,
  //           height: 200,
  //           child: Image.asset(
  //             "assets/grandpa.jpg",
  //             scale: 0.5,
  //           )),
  //       FlutterMap(
  //         mapController: _mapController,
  //         options: MapOptions(
  //           center: _latLngList[0],
  //           bounds: LatLngBounds.fromPoints(_latLngList),
  //           zoom: _zoom,
  //         ),
  //         layers: [
  //           TileLayerOptions(
  //             minZoom: 2,
  //             maxZoom: 18,
  //             backgroundColor: Colors.black,
  //             // errorImage: ,
  //             urlTemplate: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
  //             subdomains: ['a', 'b', 'c'],
  //           ),
  //         ],
  //       )
  //     ],
  //   )));
  // }
}
