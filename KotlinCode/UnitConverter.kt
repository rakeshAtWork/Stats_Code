package com.example.unitconverter

import android.os.Bundle
import android.widget.Toast
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.width
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.ArrowDropDown
import androidx.compose.material3.Button
import androidx.compose.material3.DropdownMenu
import androidx.compose.material3.DropdownMenuItem
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.ImageBitmap
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.example.unitconverter.ui.theme.UnitConverterTheme
import kotlin.math.roundToInt

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            UnitConverterTheme {
                // A surface container using the 'background' color from the theme
                Surface(
                    modifier = Modifier.fillMaxSize(),
                    color = MaterialTheme.colorScheme.background
                ) {
                        unitConvert()
                }
            }
        }
    }
}



@Composable
fun unitConvert(){
    var inputValue by remember { mutableStateOf("") }
    var outputValue by remember { mutableStateOf("") }
    var inputUnit by remember { mutableStateOf("Meters") }
    var outputUnit by remember { mutableStateOf("Meters") }
    var iExpanded by remember { mutableStateOf(false) }
    var oExpanded by remember { mutableStateOf(false) }  // here by will reflect its properties directly i.e obj.value will become only value.
    var conversionFactor = remember { mutableStateOf(1.00) }
    var oConversionFactor = remember{ mutableStateOf(1.00) }

    fun convertUnit(){
        val inputValueDouble = inputValue.toDoubleOrNull() ?: 0.0  // Elvis Operator. if the first value gives null then output will be the 2nd one.
        val result  = (inputValueDouble * conversionFactor.value *100.0/ oConversionFactor.value).roundToInt()/100.0
        outputValue = result.toString()

    }

    Column(
        modifier = Modifier.fillMaxSize(),  // To handle size and how content will viewed.
        verticalArrangement = Arrangement.Center,
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Text(text = "Unit Converter", modifier = Modifier.padding(20.dp), style = MaterialTheme.typography.headlineLarge)
        Spacer(modifier = Modifier.height(10.dp))

        OutlinedTextField(value = inputValue,
                          onValueChange ={
                          inputValue = it
                              convertUnit()
                           },
                          label = { Text(text = "Enter Value")
                          })
        Spacer(modifier = Modifier.height(10.dp))
        Row {
//            val context = LocalContext.current  // use context to make or populate toast.

            Box {
                Button(onClick = { iExpanded=true }) {
                    Text(text = inputUnit)
                    Icon( Icons.Default.ArrowDropDown, contentDescription ="" )
                }
                DropdownMenu(expanded = iExpanded, onDismissRequest = { iExpanded = false }) {
                    DropdownMenuItem(text = { Text("CentiMeter")},
                        onClick = {iExpanded = false
                                 inputUnit = "CentiMeter"
                                 conversionFactor.value = 0.01
                        })
                    DropdownMenuItem(text = { Text("Meter")},
                        onClick = { iExpanded = false
                            inputUnit = "Meter"
                            conversionFactor.value = 1.0
                            convertUnit()
                        })
                    DropdownMenuItem(text = { Text("MiliMeter")},
                        onClick = {iExpanded = false
                            inputUnit = "MiliMeter"
                            conversionFactor.value = 0.001
                            convertUnit()
                        })
                    DropdownMenuItem(text = { Text("Feet")},
                        onClick = {iExpanded = false
                            inputUnit = "Feet"
                            conversionFactor.value = 0.3048 })
                }

            }
            Spacer(modifier = Modifier.width(16.dp))
            Box{
                Button(onClick = { oExpanded = true }) {
                    Text(text = outputUnit)
                    Icon( Icons.Default.ArrowDropDown, contentDescription ="" )
                }

                DropdownMenu(expanded = oExpanded, onDismissRequest = { oExpanded= false }) {
                    DropdownMenuItem(text = { Text("CentiMeter")},
                        onClick = {
                            oExpanded = false
                            outputUnit = "CentiMeter"
                            oConversionFactor.value = 0.01
                            convertUnit()

                        })
                    DropdownMenuItem(text = { Text("Meter")},
                        onClick = {
                            oExpanded = false
                            outputUnit = "Meter"
                            oConversionFactor.value = 1.00
                            convertUnit()
                        })
                    DropdownMenuItem(text = { Text("MiliMeter")},
                        onClick = {
                            oExpanded = false
                            outputUnit = "MiliMeter"
                            oConversionFactor.value = 0.001
                            convertUnit()
                        })
                    DropdownMenuItem(text = { Text("Feet")},
                        onClick = {
                            oExpanded = false
                            outputUnit = "Feet"
                            oConversionFactor.value = 0.3048
                            convertUnit()
                        })
                }
            }
        }
        Text(text = "Result : $outputValue $outputUnit",
            style = MaterialTheme.typography.headlineMedium
            )

    }
}


//@Composable
//fun Greeting(name: String, modifier: Modifier = Modifier) {
//    Column {
//        Text(
//            text = "Hello $name!",
//            modifier = modifier
//        )
//    }
//}





//@Preview(showBackground = true)  show-Background will activate the background.
//@Composable
//fun GreetingPreview() {
//    UnitConverterTheme {
//        Column {
//            Greeting(name = "Rakesh Raushan")
//        }
//
//    }
//}



@Preview(showBackground = true)
@Composable
fun unitConverterPreview(){
    unitConvert()
}