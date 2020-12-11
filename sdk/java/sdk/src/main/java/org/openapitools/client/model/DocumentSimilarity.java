/*
 * 
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;

/**
 * DocumentSimilarity
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2020-12-11T16:57:55.511+03:00[Europe/Moscow]")
public class DocumentSimilarity {
  public static final String SERIALIZED_NAME_PK = "pk";
  @SerializedName(SERIALIZED_NAME_PK)
  private Integer pk;

  public static final String SERIALIZED_NAME_DOCUMENT_A_NAME = "document_a__name";
  @SerializedName(SERIALIZED_NAME_DOCUMENT_A_NAME)
  private String documentAName;

  public static final String SERIALIZED_NAME_DOCUMENT_A_DESCRIPTION = "document_a__description";
  @SerializedName(SERIALIZED_NAME_DOCUMENT_A_DESCRIPTION)
  private String documentADescription;

  public static final String SERIALIZED_NAME_DOCUMENT_A_PK = "document_a__pk";
  @SerializedName(SERIALIZED_NAME_DOCUMENT_A_PK)
  private String documentAPk;

  public static final String SERIALIZED_NAME_DOCUMENT_A_DOCUMENT_TYPE = "document_a__document_type";
  @SerializedName(SERIALIZED_NAME_DOCUMENT_A_DOCUMENT_TYPE)
  private String documentADocumentType;

  public static final String SERIALIZED_NAME_DOCUMENT_B_NAME = "document_b__name";
  @SerializedName(SERIALIZED_NAME_DOCUMENT_B_NAME)
  private String documentBName;

  public static final String SERIALIZED_NAME_DOCUMENT_B_DESCRIPTION = "document_b__description";
  @SerializedName(SERIALIZED_NAME_DOCUMENT_B_DESCRIPTION)
  private String documentBDescription;

  public static final String SERIALIZED_NAME_DOCUMENT_B_PK = "document_b__pk";
  @SerializedName(SERIALIZED_NAME_DOCUMENT_B_PK)
  private String documentBPk;

  public static final String SERIALIZED_NAME_DOCUMENT_B_DOCUMENT_TYPE = "document_b__document_type";
  @SerializedName(SERIALIZED_NAME_DOCUMENT_B_DOCUMENT_TYPE)
  private String documentBDocumentType;

  public static final String SERIALIZED_NAME_SIMILARITY = "similarity";
  @SerializedName(SERIALIZED_NAME_SIMILARITY)
  private String similarity;


   /**
   * Get pk
   * @return pk
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Integer getPk() {
    return pk;
  }




   /**
   * Get documentAName
   * @return documentAName
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getDocumentAName() {
    return documentAName;
  }




   /**
   * Get documentADescription
   * @return documentADescription
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getDocumentADescription() {
    return documentADescription;
  }




   /**
   * Get documentAPk
   * @return documentAPk
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getDocumentAPk() {
    return documentAPk;
  }




   /**
   * Get documentADocumentType
   * @return documentADocumentType
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getDocumentADocumentType() {
    return documentADocumentType;
  }




   /**
   * Get documentBName
   * @return documentBName
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getDocumentBName() {
    return documentBName;
  }




   /**
   * Get documentBDescription
   * @return documentBDescription
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getDocumentBDescription() {
    return documentBDescription;
  }




   /**
   * Get documentBPk
   * @return documentBPk
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getDocumentBPk() {
    return documentBPk;
  }




   /**
   * Get documentBDocumentType
   * @return documentBDocumentType
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getDocumentBDocumentType() {
    return documentBDocumentType;
  }




  public DocumentSimilarity similarity(String similarity) {
    
    this.similarity = similarity;
    return this;
  }

   /**
   * Get similarity
   * minimum: -1000
   * maximum: 1000
   * @return similarity
  **/
  @ApiModelProperty(required = true, value = "")

  public String getSimilarity() {
    return similarity;
  }


  public void setSimilarity(String similarity) {
    this.similarity = similarity;
  }


  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DocumentSimilarity documentSimilarity = (DocumentSimilarity) o;
    return Objects.equals(this.pk, documentSimilarity.pk) &&
        Objects.equals(this.documentAName, documentSimilarity.documentAName) &&
        Objects.equals(this.documentADescription, documentSimilarity.documentADescription) &&
        Objects.equals(this.documentAPk, documentSimilarity.documentAPk) &&
        Objects.equals(this.documentADocumentType, documentSimilarity.documentADocumentType) &&
        Objects.equals(this.documentBName, documentSimilarity.documentBName) &&
        Objects.equals(this.documentBDescription, documentSimilarity.documentBDescription) &&
        Objects.equals(this.documentBPk, documentSimilarity.documentBPk) &&
        Objects.equals(this.documentBDocumentType, documentSimilarity.documentBDocumentType) &&
        Objects.equals(this.similarity, documentSimilarity.similarity);
  }

  @Override
  public int hashCode() {
    return Objects.hash(pk, documentAName, documentADescription, documentAPk, documentADocumentType, documentBName, documentBDescription, documentBPk, documentBDocumentType, similarity);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class DocumentSimilarity {\n");
    sb.append("    pk: ").append(toIndentedString(pk)).append("\n");
    sb.append("    documentAName: ").append(toIndentedString(documentAName)).append("\n");
    sb.append("    documentADescription: ").append(toIndentedString(documentADescription)).append("\n");
    sb.append("    documentAPk: ").append(toIndentedString(documentAPk)).append("\n");
    sb.append("    documentADocumentType: ").append(toIndentedString(documentADocumentType)).append("\n");
    sb.append("    documentBName: ").append(toIndentedString(documentBName)).append("\n");
    sb.append("    documentBDescription: ").append(toIndentedString(documentBDescription)).append("\n");
    sb.append("    documentBPk: ").append(toIndentedString(documentBPk)).append("\n");
    sb.append("    documentBDocumentType: ").append(toIndentedString(documentBDocumentType)).append("\n");
    sb.append("    similarity: ").append(toIndentedString(similarity)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}
