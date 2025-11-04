import 'package:flutter/material.dart';

void main() => runApp(GridViewDemo());

class GridViewDemo extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'GridView Demo',
      home: Scaffold(
        appBar: AppBar(title: Text('GridView Demo')),
        body: GridView.builder(
          padding: EdgeInsets.all(8),
          gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
            crossAxisCount: 3,
            mainAxisSpacing: 8,
            crossAxisSpacing: 8,
          ),
          itemCount: 30,
          itemBuilder: (context, index) => Container(
            color: Colors.primaries[index % Colors.primaries.length],
            child: Center(child: Text('\\${index + 1}', style: TextStyle(color: Colors.white, fontSize: 18))),
          ),
        ),
      ),
    );
  }
}
