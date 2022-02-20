import 'package:flutter/material.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';

class ResultScreen extends StatefulWidget {
  const ResultScreen({Key? key}) : super(key: key);
  @override
  State<StatefulWidget> createState() => _ResultScreenState();
}

class _ResultScreenState extends State<ResultScreen> {
  var data = [
    {
      'skill_interest': 'computer science',
      'type_of_opportunity': 'courses',
      'in_person_online': 'all',
      'resource_data_dict': {
        'https://www.coursera.org/specializations/python': [
          'No prior experience required.',
          {'courses': 1}
        ],
        'https://www.coursera.org/professional-certificates/google-it-support':
            [
          'This program includes over 100 hours of instruction and hundreds of practice-based assessments, which will help you simulate real-world IT support scenarios that are critical for success in the workplace.',
          {'courses': 8}
        ],
        'https://www.coursera.org/specializations/introduction-computer-science-programming':
            [
          'There are a range of activities included in this specialization that will enable learners to apply and develop their programming skills in a fun and engaging way. Learners will master the fundamentals of computer science by solving mathematical puzzles using interactive techniques, becoming a detective and solving crimes in an interactive sleuth application and apply computer science concepts to solve problems found in daily computer use.',
          {'courses': 20, 'computer science': 6}
        ],
        'https://www.coursera.org/specializations/data-structures-algorithms': [
          'The specialization contains two real-world projects: Big Networks and Genome Assembly. You will analyze both road networks and social networks and will learn how to compute the shortest route between New York and San Francisco 1000 times faster than the shortest path algorithms you learn in the standard Algorithms 101 course! Afterwards, you will learn how to assemble genomes from millions of short fragments of DNA and how assembly algorithms fuel recent developments in personalized medicine.',
          {'courses': 24, 'computer science': 4}
        ],
        'https://www.coursera.org/learn/cs-programming-java': [
          'The basis for education in the last millennium was â\x80\x9creading, writing, and arithmetic;â\x80\x9d now it is reading, writing, and computing. Learning to program is an essential part of the education of every student, not just in the sciences and engineering, but in the arts, social sciences, and humanities, as well. Beyond direct applications, it is the first step in understanding the nature of computer scienceâ\x80\x99s undeniable impact on the modern world.  This course covers the first half of our book Computer Science: An Interdisciplinary Approach (the second half is covered in our Coursera course Computer Science: Algorithms, Theory, and Machines). Our intent is to teach programming to those who need or want to learn it, in a scientific context.',
          {'courses': 38, 'computer science': 10}
        ]
      }
    },
    {
      'skill_interest': 'cs',
      'type_of_opportunity': 'courses',
      'in_person_online': 'all',
      'resource_data_dict': {
        'https://www.coursera.org/learn/introduction-to-web-development-with-html-css-javacript':
            [
          'Want to take the first steps to become a Cloud Application Developer? This course will lead you through the languages and tools you will need to develop your own Cloud Apps.',
          {'courses': 7, 'cs': 6}
        ],
        'https://www.coursera.org/learn/website-coding': [
          'In this course you will learn three key website programming and design languages: HTML, CSS and JavaScript. You will create a web page using basic elements to control layout and style.  Additionally, your web page will support interactivity.',
          {'cs': 11, 'courses': 10}
        ],
        'https://www.coursera.org/learn/html-css-javascript-for-web-developers':
            [
          'Do you realize that the only functionality of a web application that the user directly interacts with is through the web page? Implement it poorly and, to the user, the server-side becomes irrelevant! Todayâ\x80\x99s user expects a lot out of the web page: it has to load fast, expose the desired service, and be comfortable to view on all devices: from a desktop computers to tablets and mobile phones.',
          {'courses': 18, 'cs': 6}
        ],
        'https://www.coursera.org/learn/duke-programming-web': [
          'Learn foundational programming concepts (e.g., functions, for loops, conditional statements) and how to solve problems like a programmer. In addition, learn basic web development as you build web pages using HTML, CSS, JavaScript. By the end of the course, will create a web page where others can upload their images and apply image filters that you create.',
          {'courses': 15, 'cs': 7}
        ],
        'https://www.coursera.org/learn/introcss': [
          'The web today is almost unrecognizable from the early days of white pages with lists of blue links.  Now, sites are designed with complex layouts, unique fonts, and customized color schemes.   This course will show you the basics of Cascading Style Sheets (CSS3).  The emphasis will be on learning how to write CSS rules, how to test code, and how to establish good programming habits.',
          {'courses': 14, 'cs': 14}
        ]
      }
    },
    {
      'skill_interest': 'math',
      'type_of_opportunity': 'courses',
      'in_person_online': 'all',
      'resource_data_dict': {
        'https://www.coursera.org/learn/mathematical-thinking': [
          'Learn how to think the way mathematicians do â\x80\x93 a powerful cognitive process developed over thousands of years.',
          {'math': 2, 'courses': 3}
        ],
        'https://www.coursera.org/learn/introduction-to-calculus': [
          'The focus and themes of the Introduction to Calculus course address the most important foundations for applications of mathematics in science, engineering and commerce. The course emphasises the key ideas and historical motivation for calculus, while at the same time striking a balance between theory and application, leading to a mastery of key threshold concepts in foundational mathematics.',
          {'courses': 18, 'math': 11}
        ],
        'https://www.coursera.org/learn/tsi-math-prep': [
          'The purpose of this course is to review and practice key concepts in preparation for the math portion of the Texas Success Initiative Assessment 2.0 (TSI2).Â\xa0 The TSI2 is series of placement tests for learners enrolling in public universities in Texas.Â\xa0 This MOOC will cover the four main categories of the Mathematics portion:Â\xa0 Quantitative Reasoning, Algebraic Reasoning, Geometric & Spatial Reasoning, and Probabilistic & Statistical Reasoning.Â',
          {'math': 7, 'courses': 19}
        ],
        'https://www.coursera.org/specializations/algebra-elementary-to-advanced':
            [
          'Instead of a single large project, there are many smaller applied and algebra problems throughout the modules of the courses. Practice problems with worked solutions are provided throughout the course to prepare students and allow them to be successful. Problems range in difficulty to allow students to be challenged as they apply the knowledge gained from the course.',
          {'courses': 11, 'math': 6}
        ],
        'https://www.coursera.org/specializations/mathematics-machine-learning':
            [
          'Through the assignments of this specialisation you will use the skills you have learned to produce mini-projects with Python on interactive notebooks, an easy to learn tool which will help you apply the knowledge to real world problems. For example, using linear algebra in order to calculate the page rank of a small simulated internet, applying multivariate calculus in order to train your own neural network, performing a non-linear least squares regression to fit a model to a data set, and using principal component analysis to determine the features of the MNIST digits data set.',
          {'courses': 22, 'math': 17}
        ]
      }
    },
    {
      'skill_interest': 'machine learning',
      'type_of_opportunity': 'courses',
      'in_person_online': 'all',
      'resource_data_dict': {
        'https://www.coursera.org/specializations/deep-learning': [
          'By the end youâ\x80\x99ll be able to',
          {'courses': 1}
        ],
        'https://www.coursera.org/specializations/machine-learning': [
          'Learners will implement and apply predictive, classification, clustering, and information retrieval machine learning algorithms to real datasets throughout each course in the specialization. They will walk away with applied machine learning and Python programming experience.',
          {'machine learning': 7, 'courses': 13}
        ],
        'https://www.coursera.org/specializations/deep-learning-healthcare': [
          'Learners will be able to apply the theoretical concepts in autograded programming assignments that use training data we provide for use with different types of neural networking algorithms. The technology used is (among others) Jupyter Notebooks / PyTorch.',
          {'machine learning': 1, 'courses': 11}
        ],
        'https://www.coursera.org/professional-certificates/ibm-machine-learning':
            [
          'This Professional Certificate has a strong emphasis on developing the skills that help you advance a career in Machine Learning. All the courses include a series of hands-on labs and final projects that help you focus on a specific project that interests you. Throughout this Professional Certificate, you will gain exposure to a series of tools, libraries, cloud services, datasets, algorithms, assignments and projects that will provide you with practical skills with applicability to Machine Learning jobs. These skills include:',
          {'courses': 25, 'machine learning': 4}
        ],
        'https://www.coursera.org/learn/machine-learning': [
          "Machine learning is the science of getting computers to act without being explicitly programmed. In the past decade, machine learning has given us self-driving cars, practical speech recognition, effective web search, and a vastly improved understanding of the human genome. Machine learning is so pervasive today that you probably use it dozens of times a day without knowing it. Many researchers also think it is the best way to make progress towards human-level AI. In this class, you will learn about the most effective machine learning techniques, and gain practice implementing them and getting them to work for yourself. More importantly, you'll learn about not only the theoretical underpinnings of learning, but also gain the practical know-how needed to quickly and powerfully apply these techniques to new problems. Finally, you'll learn about some of Silicon Valley's best practices in innovation as it pertains to machine learning and AI.",
          {'machine learning': 14, 'courses': 28}
        ]
      }
    },
    {
      'skill_interest': 'probability',
      'type_of_opportunity': 'courses',
      'in_person_online': 'all',
      'resource_data_dict': {
        'https://www.coursera.org/specializations/probabilistic-graphical-models':
            [
          'Through various lectures, quizzes, programming assignments and exams, learners in this specialization will practice and master the fundamentals of probabilistic graphical models. This specialization has three five-week courses for a total of fifteen weeks.',
          {'courses': 13, 'probability': 1}
        ],
        'https://www.coursera.org/learn/introductiontoprobability': [
          'This course will provide you with a basic, intuitive and practical introduction into Probability Theory. You will be able to learn how to apply Probability Theory in different scenarios and you will earn a "toolbox" of methods to deal with uncertainty in your daily life.',
          {'courses': 9, 'probability': 5}
        ],
        'https://www.coursera.org/specializations/statistical-inference-for-data-science-applications':
            [
          'Learners will practice new probability skills. including fundamental statistical analysis of data sets, by completing exercises in Jupyter Notebooks. In addition, learners will test their knowledge by completing benchmark quizzes throughout the courses.',
          {'courses': 11, 'probability': 4}
        ],
        'https://www.coursera.org/learn/probability-theory-foundation-for-data-science':
            [
          'Understand the foundations of probability and its relationship to statistics and data science.Â\xa0 Weâ\x80\x99ll learn what it means to calculate a probability, independent and dependent outcomes, and conditional events.Â\xa0 Weâ\x80\x99ll study discrete and continuous random variables and see how this fits with data collection.Â\xa0 Weâ\x80\x99ll end the course with Gaussian (normal) random variables and the Central Limit Theorem and understand its fundamental importance for all of statistics and data science.',
          {'courses': 18, 'probability': 7}
        ],
        'https://www.coursera.org/learn/stanford-statistics': [
          'Stanford\'s "Introduction to Statistics" teaches you statistical thinking concepts that are essential for learning from data and communicating insights. By the end of the course,Â\xa0you will be able to perform exploratory data analysis, understand key principles of sampling, and select appropriate tests of significance for multiple contexts. You will gain the foundational skills that prepare you to pursue more advanced topics in statistical thinking and machine learning.',
          {'courses': 11, 'probability': 3}
        ]
      }
    }
  ];

  get testMap => null;

  @override
  Widget build(BuildContext context) {
    print(data[0]["skill_interest"]);
    return SafeArea(child: _loading());
  }

  Widget _loading() {
    if (data.isEmpty) {
      return Center(child: SpinKitFadingCircle());
    } else {
      return Container(
          child: SafeArea(
        child: Column(
          mainAxisSize: MainAxisSize.max,
          children: [
            Row(
              children: [
                SizedBox(
                    height: 50,
                    width: MediaQuery.of(context).size.width,
                    child: ListView.builder(
                        shrinkWrap: true,
                        itemBuilder: (_, index) {
                          return SizedBox(
                            height: 50,
                            width: MediaQuery.of(context).size.width / 6,
                            child: ElevatedButton(
                                onPressed: () {},
                                child: Text(data[index - 1]["skill_interest"]
                                    .toString())),
                          );
                        }))
              ],
            ),
          ],
        ),
      ));
    }
  }
}
