import 'package:blair_hacks_2022/colors.dart';
import 'package:flutter/material.dart';
import 'package:dio/dio.dart';
import 'package:location/location.dart';
import 'package:card_swiper/card_swiper.dart';
import 'package:geocoding/geocoding.dart' as geocoder;
import 'package:animated_custom_dropdown/custom_dropdown.dart';

class Homescreen extends StatefulWidget {
  const Homescreen({Key? key}) : super(key: key);
  @override
  State<StatefulWidget> createState() => _HomescreenState();
}

class _HomescreenState extends State<Homescreen> {
  static List<String> skillsList = [];
  static List<String> interestsList = [];
  static List<String> languagesList = [];
  static List<String> oppurtunityTypeList = [];
  static List<String> virtualOrInPersonList = [];

  var searchedItems = [
    oppurtunityTypeList,
    virtualOrInPersonList,
    skillsList,
    interestsList,
    languagesList,
  ];
  var gradesList = [
    'Pre-K',
    'Kindergarten',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10',
    '11',
    '12',
    'Post-Grad'
  ];
  var oppurtunitiesList = ['Courses', 'Volunteer', 'Sports', 'Tutoring'];
  List<String> categories = [
    'Type Of Opportunity',
    'In Person/Virtual',
    'Skills',
    'Interests',
    'Languages',
  ];
  var sportsList = [
    'Archery',
    'Badminton',
    'Baseball',
    "Basketball - Women's",
    'Basketball-Boys',
    'Basketball-Girls',
    "Basketball-Men's",
    'Baton Twirling',
    'Bowling',
    'Cheerleading',
    'Chess',
    'Cornhole',
    'Cricket',
    'Dance',
    'Diving',
    'Esports',
    'Fencing',
    'Field Hockey',
    'Football - Flag, 7v7',
    'Football Cheer',
    'Football Tackle',
    'Futsal',
    "Girls & Women's Flag Football",
    'Golf',
    'Gymnastics',
    'Gymnastics - Acrobatic',
    'Hockey - Collegiate',
    'Hockey - Ice',
    'Hockey - Inline',
    'Hockey - Junior A Hockey',
    'Jiu Jitsu',
    'Judo',
    'Jump Rope',
    'Karate',
    'Kung-Fu',
    'Lacrosse',
    'Paddle Board',
    'Pickleball',
    'Powerlifting',
    'Rhythmic Gymnastics',
    'Skateboarding',
    'Soccer',
    'Softball',
    'Special Needs',
    'Sport Stacking',
    'Surfing',
    'Swimming',
    'Table Tennis',
    'Taekwondo',
    'Target Shooting',
    'Team Handball',
    'Tennis',
    'Track and Field',
    'Trampoline - Tumbling',
    'Volleyball',
    'Water Polo',
    'Weightlifting',
    'Wrestling'
  ];
  int indexter = 0;
  var _selected = '';
  var _selectedGrade = '';
  bool coolnessEnabled = true;
  TextEditingController textEditingController = TextEditingController();
  final infoSelectionController = TextEditingController();
  final secondInfoSelectionController = TextEditingController();
  final thirdInfoSelectionController = TextEditingController();
  var _selectedSports = '';

  String _inPersonOrVirtual = '';
  @override
  Widget build(BuildContext context) {
    return Container(
        decoration: BoxDecoration(
          gradient: LinearGradient(
            begin: Alignment.bottomCenter,
            end: Alignment.topCenter,
            stops: const [0.1, 0.5, 0.7, 0.9],
            colors: [
              Colors.white,
              gradientColor,
              gradientColor,
              Colors.white,
            ],
          ),
        ),
        child: SafeArea(
            child: Padding(
                padding: const EdgeInsets.all(8.0),
                child: Column(
                  children: [
                    Text(
                      'NAME HERE',
                      style: TextStyle(
                        fontWeight: FontWeight.bold,
                        color: accentColor,
                        fontSize: 50,
                      ),
                    ),
                    const Padding(padding: EdgeInsets.only(bottom: 30)),
                    SizedBox(
                      height: MediaQuery.of(context).size.height / 1.6,
                      width: MediaQuery.of(context).size.width,
                      child: Swiper(
                          control: SwiperControl(
                            color: accentColor,
                          ),
                          pagination: SwiperPagination(
                            alignment: Alignment.bottomCenter,
                            builder: DotSwiperPaginationBuilder(
                                color: Colors.grey, activeColor: accentColor),
                          ),
                          // control: SwiperControl(
                          //   color: accentColor,
                          // ),
                          scrollDirection: Axis.horizontal,
                          itemCount: categories.length,
                          onIndexChanged: (index) {
                            setState(() {
                              indexter = index;
                              textEditingController.clear();
                            });
                          },
                          itemBuilder: (context, pageViewIndex) {
                            if (pageViewIndex == 0) {
                              return Card(
                                shadowColor: Color.fromARGB(35, 158, 158, 158),
                                shape: RoundedRectangleBorder(
                                  borderRadius: BorderRadius.circular(50),
                                ),
                                borderOnForeground: false,
                                elevation: 20,
                                color: backgroundColor,
                                child: Center(
                                  child: Padding(
                                    padding: const EdgeInsets.all(8.0),
                                    child: Column(
                                      mainAxisAlignment:
                                          MainAxisAlignment.center,
                                      children: [
                                        Text(
                                          categories[pageViewIndex],
                                          style: TextStyle(
                                            fontWeight: FontWeight.bold,
                                            color: accentColor,
                                            fontSize: 30,
                                          ),
                                        ),
                                        SizedBox(
                                          width:
                                              MediaQuery.of(context).size.width,
                                          child: Column(
                                            mainAxisAlignment:
                                                MainAxisAlignment.center,
                                            children: [
                                              CustomDropdown(
                                                  items: oppurtunitiesList,
                                                  controller:
                                                      infoSelectionController,
                                                  onChanged: (selected) {
                                                    setState(() {
                                                      _selected = selected;
                                                    });
                                                  }),
                                              firstInstanceChange(),
                                            ],
                                          ),
                                        ),
                                        SizedBox(
                                          height: 40,
                                          child: ListView.builder(
                                              physics:
                                                  const ClampingScrollPhysics(),
                                              shrinkWrap: true,
                                              itemCount:
                                                  searchedItems[pageViewIndex]
                                                      .length,
                                              scrollDirection: Axis.horizontal,
                                              itemBuilder: (context, index) {
                                                if (searchedItems[pageViewIndex]
                                                    .isEmpty) {
                                                  return const SizedBox
                                                      .shrink();
                                                } else {
                                                  return Padding(
                                                      padding:
                                                          const EdgeInsets.only(
                                                              right: 20),
                                                      child: Container(
                                                        decoration:
                                                            BoxDecoration(
                                                          color: accentColor,
                                                          borderRadius:
                                                              BorderRadius
                                                                  .circular(20),
                                                        ),
                                                        child: Padding(
                                                          padding:
                                                              const EdgeInsets
                                                                      .only(
                                                                  left: 10,
                                                                  right: 10),
                                                          child: Row(
                                                            children: [
                                                              Text(
                                                                searchedItems[
                                                                        pageViewIndex]
                                                                    .elementAt(
                                                                        index),
                                                              ),
                                                              ElevatedButton(
                                                                  style: ButtonStyle(
                                                                      shadowColor:
                                                                          MaterialStateProperty.all(Colors
                                                                              .transparent),
                                                                      backgroundColor:
                                                                          MaterialStateProperty.all(Colors
                                                                              .transparent)),
                                                                  onPressed:
                                                                      () {
                                                                    setState(
                                                                        () {
                                                                      searchedItems[
                                                                              pageViewIndex]
                                                                          .remove(searchedItems[pageViewIndex]
                                                                              [
                                                                              index]);
                                                                    });
                                                                  },
                                                                  child:
                                                                      Container(
                                                                    decoration:
                                                                        BoxDecoration(
                                                                      color: Colors
                                                                              .blueGrey[
                                                                          700],
                                                                      borderRadius:
                                                                          BorderRadius.circular(
                                                                              20),
                                                                    ),
                                                                    child:
                                                                        const Icon(
                                                                      Icons
                                                                          .remove,
                                                                      color: Colors
                                                                          .black,
                                                                    ),
                                                                  )),
                                                            ],
                                                          ),
                                                        ),
                                                      ));
                                                }
                                              }),
                                        ),
                                        Padding(
                                            padding: EdgeInsets.only(
                                                top: MediaQuery.of(context)
                                                        .size
                                                        .height /
                                                    4)),
                                      ],
                                    ),
                                  ),
                                ),
                              );
                            } else if (pageViewIndex == 1) {
                              return Container(
                                decoration: BoxDecoration(
                                  borderRadius: BorderRadius.circular(50),
                                ),
                                child: Card(
                                  shape: RoundedRectangleBorder(
                                    borderRadius: BorderRadius.circular(50),
                                  ),
                                  borderOnForeground: false,
                                  elevation: 20,
                                  shadowColor:
                                      Color.fromARGB(35, 158, 158, 158),
                                  color: backgroundColor,
                                  child: Padding(
                                    padding: const EdgeInsets.all(8.0),
                                    child: SizedBox(
                                      height:
                                          MediaQuery.of(context).size.height /
                                              2,
                                      child: Column(
                                        mainAxisAlignment:
                                            MainAxisAlignment.center,
                                        children: [
                                          Text(
                                            categories[pageViewIndex],
                                            style: TextStyle(
                                              fontWeight: FontWeight.bold,
                                              color: accentColor,
                                              fontSize: 30,
                                            ),
                                          ),
                                          SizedBox(
                                            width: MediaQuery.of(context)
                                                .size
                                                .width,
                                            child: Column(
                                              children: [
                                                CustomDropdown(
                                                    items: const [
                                                      'In-Person',
                                                      'Virtual',
                                                      'No Preference'
                                                    ],
                                                    controller:
                                                        thirdInfoSelectionController,
                                                    onChanged: (selected) {
                                                      setState(() {
                                                        _inPersonOrVirtual =
                                                            selected;
                                                      });
                                                    }),
                                              ],
                                            ),
                                          ),
                                          SizedBox(
                                            height: 40,
                                            child: ListView.builder(
                                                physics:
                                                    const ClampingScrollPhysics(),
                                                shrinkWrap: true,
                                                itemCount:
                                                    searchedItems[pageViewIndex]
                                                        .length,
                                                scrollDirection:
                                                    Axis.horizontal,
                                                itemBuilder: (context, index) {
                                                  if (searchedItems[
                                                          pageViewIndex]
                                                      .isEmpty) {
                                                    return const SizedBox
                                                        .shrink();
                                                  } else {
                                                    return Padding(
                                                        padding:
                                                            const EdgeInsets
                                                                    .only(
                                                                right: 20),
                                                        child: Container(
                                                          decoration:
                                                              BoxDecoration(
                                                            color: accentColor,
                                                            borderRadius:
                                                                BorderRadius
                                                                    .circular(
                                                                        20),
                                                          ),
                                                          child: Padding(
                                                            padding:
                                                                const EdgeInsets
                                                                        .only(
                                                                    left: 10,
                                                                    right: 10),
                                                            child: Row(
                                                              children: [
                                                                Text(
                                                                  searchedItems[
                                                                          pageViewIndex]
                                                                      .elementAt(
                                                                          index),
                                                                ),
                                                                ElevatedButton(
                                                                    style: ButtonStyle(
                                                                        shadowColor:
                                                                            MaterialStateProperty.all(Colors
                                                                                .transparent),
                                                                        backgroundColor:
                                                                            MaterialStateProperty.all(Colors
                                                                                .transparent)),
                                                                    onPressed:
                                                                        () {
                                                                      setState(
                                                                          () {
                                                                        searchedItems[pageViewIndex].remove(searchedItems[pageViewIndex]
                                                                            [
                                                                            index]);
                                                                      });
                                                                    },
                                                                    child:
                                                                        Container(
                                                                      decoration:
                                                                          BoxDecoration(
                                                                        color: Colors
                                                                            .blueGrey[700],
                                                                        borderRadius:
                                                                            BorderRadius.circular(20),
                                                                      ),
                                                                      child:
                                                                          const Icon(
                                                                        Icons
                                                                            .remove,
                                                                        color: Colors
                                                                            .black,
                                                                      ),
                                                                    )),
                                                              ],
                                                            ),
                                                          ),
                                                        ));
                                                  }
                                                }),
                                          ),
                                          Padding(
                                              padding: EdgeInsets.only(
                                                  top: MediaQuery.of(context)
                                                          .size
                                                          .height /
                                                      4)),
                                        ],
                                      ),
                                    ),
                                  ),
                                ),
                              );
                            }
                            return Container(
                              decoration: BoxDecoration(
                                borderRadius: BorderRadius.circular(50),
                              ),
                              child: Card(
                                shape: RoundedRectangleBorder(
                                  borderRadius: BorderRadius.circular(50),
                                ),
                                borderOnForeground: false,
                                elevation: 20,
                                shadowColor: Color.fromARGB(35, 158, 158, 158),
                                color: backgroundColor,
                                child: Padding(
                                  padding: const EdgeInsets.all(8.0),
                                  child: SizedBox(
                                    height:
                                        MediaQuery.of(context).size.height / 2,
                                    child: Column(
                                      mainAxisAlignment:
                                          MainAxisAlignment.center,
                                      children: [
                                        Text(
                                          categories[pageViewIndex],
                                          style: TextStyle(
                                            fontWeight: FontWeight.bold,
                                            color: accentColor,
                                            fontSize: 30,
                                          ),
                                        ),
                                        Padding(
                                            padding: EdgeInsets.only(top: 30)),
                                        Padding(
                                            padding: EdgeInsets.only(
                                                bottom: MediaQuery.of(context)
                                                        .size
                                                        .height /
                                                    10)),
                                        SizedBox(
                                          height: 40,
                                          child: ListView.builder(
                                              physics:
                                                  const ClampingScrollPhysics(),
                                              shrinkWrap: true,
                                              itemCount:
                                                  searchedItems[pageViewIndex]
                                                      .length,
                                              scrollDirection: Axis.horizontal,
                                              itemBuilder: (context, index) {
                                                if (searchedItems[pageViewIndex]
                                                    .isEmpty) {
                                                  return const SizedBox
                                                      .shrink();
                                                } else {
                                                  return Padding(
                                                      padding:
                                                          const EdgeInsets.only(
                                                              right: 20),
                                                      child: Container(
                                                        decoration:
                                                            BoxDecoration(
                                                          color: gradientColor,
                                                          borderRadius:
                                                              BorderRadius
                                                                  .circular(20),
                                                        ),
                                                        child: Padding(
                                                          padding:
                                                              const EdgeInsets
                                                                      .only(
                                                                  left: 10,
                                                                  right: 10),
                                                          child: Row(
                                                            children: [
                                                              Text(
                                                                searchedItems[
                                                                        pageViewIndex]
                                                                    .elementAt(
                                                                        index),
                                                              ),
                                                              ElevatedButton(
                                                                  style: ButtonStyle(
                                                                      shadowColor:
                                                                          MaterialStateProperty.all(Colors
                                                                              .transparent),
                                                                      backgroundColor:
                                                                          MaterialStateProperty.all(Colors
                                                                              .transparent)),
                                                                  onPressed:
                                                                      () {
                                                                    setState(
                                                                        () {
                                                                      searchedItems[
                                                                              pageViewIndex]
                                                                          .remove(searchedItems[pageViewIndex]
                                                                              [
                                                                              index]);
                                                                    });
                                                                  },
                                                                  child:
                                                                      Container(
                                                                    decoration:
                                                                        BoxDecoration(
                                                                      color: Colors
                                                                              .blueGrey[
                                                                          700],
                                                                      borderRadius:
                                                                          BorderRadius.circular(
                                                                              20),
                                                                    ),
                                                                    child:
                                                                        const Icon(
                                                                      Icons
                                                                          .remove,
                                                                      color: Colors
                                                                          .black,
                                                                    ),
                                                                  )),
                                                            ],
                                                          ),
                                                        ),
                                                      ));
                                                }
                                              }),
                                        ),
                                        SizedBox(
                                          height: 40,
                                          width:
                                              MediaQuery.of(context).size.width,
                                          child: TextField(
                                            controller: textEditingController,
                                            decoration: InputDecoration(
                                              focusedBorder: InputBorder.none,
                                              hintText: 'Input...',
                                              hintStyle: TextStyle(
                                                color: accentColor,
                                              ),
                                            ),
                                            onSubmitted: (value) {
                                              setState(() {
                                                searchedItems[pageViewIndex]
                                                    .add(value);
                                                textEditingController.clear();
                                              });
                                            },
                                          ),
                                        ),
                                      ],
                                    ),
                                  ),
                                ),
                              ),
                            );
                          }),
                    ),
                    Padding(
                      padding: const EdgeInsets.only(top: 30),
                      child: SizedBox(
                        child: _searchButton(),
                        width: MediaQuery.of(context).size.width / 1.1,
                      ),
                    ),
                  ],
                ))));
  }

  void _initialSearch(List<List<String>> value) async {
    Location location = Location();

    bool _serviceEnabled;
    PermissionStatus _permissionGranted;
    LocationData _locationData;

    _serviceEnabled = await location.serviceEnabled();
    if (!_serviceEnabled) {
      _serviceEnabled = await location.requestService();
      if (!_serviceEnabled) {
        return;
      }
    }

    _permissionGranted = await location.hasPermission();
    if (_permissionGranted == PermissionStatus.denied) {
      _permissionGranted = await location.requestPermission();
      if (_permissionGranted != PermissionStatus.granted) {
        return;
      }
    }

    _locationData = await location.getLocation();
    List<geocoder.Placemark> placemarks =
        await geocoder.placemarkFromCoordinates(
            _locationData.latitude!, _locationData.longitude!);
    var locationDataString;
    print(placemarks);
    //TODO: for location also pre for pre-k k for kindergarten, post for post-grad hyphenate in-person
    if (placemarks[0].isoCountryCode! == 'US') {
      locationDataString = placemarks[0].name! +
          ' ' +
          placemarks[0].administrativeArea! +
          ' ' +
          'USA';
    } else {
      locationDataString = placemarks[0].name! +
          ' ' +
          placemarks[0].administrativeArea! +
          ' ' +
          placemarks[0].isoCountryCode!;
    }

    if (_selectedSports.isNotEmpty) {
      locationDataString = locationDataString + ' ' + placemarks[0].postalCode;
    }

    if (_inPersonOrVirtual.toLowerCase() == 'no preference') {
      _inPersonOrVirtual = 'all';
    }

    var skillsLowercaseList = [];
    for (String i in value[2]) {
      skillsLowercaseList.add('"' + i.toLowerCase() + '"');
    }

    var interestsLowercaseList = [];
    for (String i in value[3]) {
      interestsLowercaseList.add('"' + i.toLowerCase() + '"');
    }

    var langaugesLowercaseList = [];
    for (String i in value[4]) {
      langaugesLowercaseList.add('"' + i.toLowerCase() + '"');
    }

    Map<String, dynamic> passingToAPIMap = {};
    if (_selectedSports.isNotEmpty) {
      passingToAPIMap["sport"] = _selectedSports;
      passingToAPIMap["location"] = locationDataString;
    } else {
      passingToAPIMap["skills"] = skillsLowercaseList;
      passingToAPIMap["interests"] = interestsLowercaseList;
      passingToAPIMap["languages"] = langaugesLowercaseList;
      passingToAPIMap["type_of_oppurtunity"] =
          '"' + _selected.toLowerCase() + '"';
      passingToAPIMap["in_person_online"] =
          '"' + _inPersonOrVirtual.toLowerCase() + '"';
      passingToAPIMap["location"] = '"' + locationDataString + '"';
      passingToAPIMap["sport"] = '"' + _selectedSports + '"';
      passingToAPIMap["grade_level"] = '"' + _selectedGrade.toLowerCase() + '"';
    }
    Dio _dio = Dio();
    var queryParameters = passingToAPIMap;
    var data = await _dio.get(
        'https://coronasafe-flask-app.herokuapp.com/getPlaces',
        queryParameters: queryParameters);
    passingToAPIMap.clear();
  }

  Widget _searchButton() {
    // if (indexter == 5) {
    return ElevatedButton(
        style: ButtonStyle(
          shape: MaterialStateProperty.all(
            RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(30),
            ),
          ),
          backgroundColor: MaterialStateProperty.all(accentColor),
        ),
        onPressed: () => _initialSearch(searchedItems),
        child: const Text('Search'));
  }

  Widget firstInstanceChange() {
    if (_selected.toLowerCase() == 'sports') {
      return CustomDropdown(
          items: sportsList,
          controller: secondInfoSelectionController,
          onChanged: (selected) {
            _selectedSports = selected;
          });
    } else if (_selected.toLowerCase() == 'tutoring') {
      return CustomDropdown(
          items: gradesList,
          controller: secondInfoSelectionController,
          onChanged: (selected) {
            _selectedGrade = selected;
          });
    } else {
      return const SizedBox.shrink();
    }
  }
}
