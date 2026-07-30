import RHBridge.P2RoundedFlatFactorCheckpoint15
import RHBridge.P2RoundedMomentLengths15
import RHBridge.P2RoundedMomentCheckpointCheck15_moments
import RHBridge.P2RoundedMomentCheckpointCheck15_mode0
import RHBridge.P2RoundedMomentCheckpointCheck15_mode1
import RHBridge.P2RoundedMomentCheckpointCheck15_mode2
import RHBridge.P2RoundedMomentCheckpointCheck15_mode3
import RHBridge.P2RoundedMomentCheckpointCheck15_mode4
import RHBridge.P2RoundedMomentCheckpointCheck15_mode5
import RHBridge.P2RoundedMomentCheckpointCheck15_mode6
import RHBridge.P2RoundedMomentCheckpointCheck15_mode7
import RHBridge.P2RoundedMomentCheckpointCheck15_mode8
import RHBridge.P2RoundedMomentCheckpointCheck15_mode9
import RHBridge.P2RoundedMomentCheckpointCheck15_mode10
import RHBridge.P2RoundedMomentCheckpointCheck15_mode11
import RHBridge.P2RoundedMomentCheckpointCheck15_mode12
import RHBridge.P2RoundedMomentCheckpointCheck15_mode13
import RHBridge.P2RoundedMomentCheckpointCheck15_mode14
import RHBridge.P2RoundedMomentCheckpointCheck15_mode15
import RHBridge.P2RoundedMomentCheckpointCheck15_mode16
import RHBridge.P2RoundedMomentCheckpointCheck15_mode17
import RHBridge.P2RoundedMomentCheckpointCheck15_mode18
import RHBridge.P2RoundedMomentCheckpointCheck15_mode19
import RHBridge.P2RoundedMomentCheckpointCheck15_mode20
import RHBridge.P2RoundedMomentCheckpointCheck15_mode21
import RHBridge.P2RoundedMomentCheckpointCheck15_mode22
import RHBridge.P2RoundedMomentCheckpointCheck15_mode23
import RHBridge.P2RoundedMomentCheckpointCheck15_mode24
import RHBridge.P2RoundedMomentCheckpointCheck15_mode25
import RHBridge.P2RoundedMomentCheckpointCheck15_mode26
import RHBridge.P2RoundedMomentCheckpointCheck15_mode27
import RHBridge.P2RoundedMomentCheckpointCheck15_mode28
import RHBridge.P2RoundedMomentCheckpointCheck15_mode29
import RHBridge.P2RoundedMomentCheckpointCheck15_mode30
import RHBridge.P2RoundedMomentCheckpointCheck15_mode31
import RHBridge.P2RoundedMomentCheckpointCheck15_mode32
import RHBridge.P2RoundedMomentCheckpointCheck15_mode33
import RHBridge.P2RoundedMomentCheckpointCheck15_mode34
import RHBridge.P2RoundedMomentCheckpointCheck15_mode35
import RHBridge.P2RoundedMomentCheckpointCheck15_mode36
import RHBridge.P2RoundedMomentCheckpointCheck15_mode37
import RHBridge.P2RoundedMomentCheckpointCheck15_mode38
import RHBridge.P2RoundedMomentCheckpointCheck15_mode39
import RHBridge.P2RoundedMomentCheckpointCheck15_mode40
import RHBridge.P2RoundedMomentCheckpointCheck15_mode41
import RHBridge.P2RoundedMomentCheckpointCheck15_mode42
import RHBridge.P2RoundedMomentCheckpointCheck15_mode43
import RHBridge.P2RoundedMomentCheckpointCheck15_mode44
import RHBridge.P2RoundedMomentCheckpointCheck15_mode45
import RHBridge.P2RoundedMomentCheckpointCheck15_mode46
import RHBridge.P2RoundedMomentCheckpointCheck15_mode47

namespace RHP2Bridge

open P2RoundedSharedEvaluator
open P2RoundedMomentRefinement

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

private theorem vector_ext_fin
    {α : Type} {n : Nat} {v w : Vector α n}
    (h : ∀ i : Fin n, v.get i = w.get i) : v = w := by
  apply Vector.ext
  intro i hi
  exact h ⟨i, hi⟩

theorem panel15DefectMoments_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.moments =
      P2RoundedTripleMoment.defectMoments
        P2RoundedFactorCheckpointData.panel15FlatCache.defect.coeffs := by
  apply vector_ext_fin
  intro row
  rw [P2RoundedTripleMoment.defectMoments_get]
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15DefectMomentRange0) panel15DefectMomentRange64) panel15DefectMomentRange128) panel15DefectMomentRange192) panel15DefectMomentRange256) row

theorem panel15Mode0MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .even ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .even ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode0MatVecRange0) panel15Mode0MatVecRange32) panel15Mode0MatVecRange64) panel15Mode0MatVecRange96) panel15Mode0MatVecRange128) row

theorem panel15Mode1MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .odd ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .odd ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode1MatVecRange0) panel15Mode1MatVecRange32) panel15Mode1MatVecRange64) panel15Mode1MatVecRange96) panel15Mode1MatVecRange128) row

theorem panel15Mode2MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .even ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .even ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode2MatVecRange0) panel15Mode2MatVecRange32) panel15Mode2MatVecRange64) panel15Mode2MatVecRange96) panel15Mode2MatVecRange128) row

theorem panel15Mode3MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .odd ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .odd ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode3MatVecRange0) panel15Mode3MatVecRange32) panel15Mode3MatVecRange64) panel15Mode3MatVecRange96) panel15Mode3MatVecRange128) row

theorem panel15Mode4MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .even ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .even ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode4MatVecRange0) panel15Mode4MatVecRange32) panel15Mode4MatVecRange64) panel15Mode4MatVecRange96) panel15Mode4MatVecRange128) row

theorem panel15Mode5MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .odd ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .odd ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode5MatVecRange0) panel15Mode5MatVecRange32) panel15Mode5MatVecRange64) panel15Mode5MatVecRange96) panel15Mode5MatVecRange128) row

theorem panel15Mode6MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .even ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .even ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode6MatVecRange0) panel15Mode6MatVecRange32) panel15Mode6MatVecRange64) panel15Mode6MatVecRange96) panel15Mode6MatVecRange128) row

theorem panel15Mode7MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .odd ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .odd ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode7MatVecRange0) panel15Mode7MatVecRange32) panel15Mode7MatVecRange64) panel15Mode7MatVecRange96) panel15Mode7MatVecRange128) row

theorem panel15Mode8MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .even ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .even ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode8MatVecRange0) panel15Mode8MatVecRange32) panel15Mode8MatVecRange64) panel15Mode8MatVecRange96) panel15Mode8MatVecRange128) row

theorem panel15Mode9MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .odd ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .odd ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode9MatVecRange0) panel15Mode9MatVecRange32) panel15Mode9MatVecRange64) panel15Mode9MatVecRange96) panel15Mode9MatVecRange128) row

theorem panel15Mode10MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .even ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .even ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode10MatVecRange0) panel15Mode10MatVecRange32) panel15Mode10MatVecRange64) panel15Mode10MatVecRange96) panel15Mode10MatVecRange128) row

theorem panel15Mode11MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .odd ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .odd ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode11MatVecRange0) panel15Mode11MatVecRange32) panel15Mode11MatVecRange64) panel15Mode11MatVecRange96) panel15Mode11MatVecRange128) row

theorem panel15Mode12MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .even ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .even ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode12MatVecRange0) panel15Mode12MatVecRange32) panel15Mode12MatVecRange64) panel15Mode12MatVecRange96) panel15Mode12MatVecRange128) row

theorem panel15Mode13MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .odd ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .odd ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode13MatVecRange0) panel15Mode13MatVecRange32) panel15Mode13MatVecRange64) panel15Mode13MatVecRange96) panel15Mode13MatVecRange128) row

theorem panel15Mode14MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .even ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .even ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode14MatVecRange0) panel15Mode14MatVecRange32) panel15Mode14MatVecRange64) panel15Mode14MatVecRange96) panel15Mode14MatVecRange128) row

theorem panel15Mode15MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .odd ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .odd ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode15MatVecRange0) panel15Mode15MatVecRange32) panel15Mode15MatVecRange64) panel15Mode15MatVecRange96) panel15Mode15MatVecRange128) row

theorem panel15Mode16MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .even ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .even ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode16MatVecRange0) panel15Mode16MatVecRange32) panel15Mode16MatVecRange64) panel15Mode16MatVecRange96) panel15Mode16MatVecRange128) row

theorem panel15Mode17MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .odd ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .odd ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode17MatVecRange0) panel15Mode17MatVecRange32) panel15Mode17MatVecRange64) panel15Mode17MatVecRange96) panel15Mode17MatVecRange128) row

theorem panel15Mode18MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .even ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .even ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode18MatVecRange0) panel15Mode18MatVecRange32) panel15Mode18MatVecRange64) panel15Mode18MatVecRange96) panel15Mode18MatVecRange128) row

theorem panel15Mode19MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .odd ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .odd ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode19MatVecRange0) panel15Mode19MatVecRange32) panel15Mode19MatVecRange64) panel15Mode19MatVecRange96) panel15Mode19MatVecRange128) row

theorem panel15Mode20MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .even ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .even ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode20MatVecRange0) panel15Mode20MatVecRange32) panel15Mode20MatVecRange64) panel15Mode20MatVecRange96) panel15Mode20MatVecRange128) row

theorem panel15Mode21MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .odd ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .odd ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode21MatVecRange0) panel15Mode21MatVecRange32) panel15Mode21MatVecRange64) panel15Mode21MatVecRange96) panel15Mode21MatVecRange128) row

theorem panel15Mode22MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .even ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .even ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode22MatVecRange0) panel15Mode22MatVecRange32) panel15Mode22MatVecRange64) panel15Mode22MatVecRange96) panel15Mode22MatVecRange128) row

theorem panel15Mode23MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .odd ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .odd ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode23MatVecRange0) panel15Mode23MatVecRange32) panel15Mode23MatVecRange64) panel15Mode23MatVecRange96) panel15Mode23MatVecRange128) row

theorem panel15Mode24MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .even ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .even ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode24MatVecRange0) panel15Mode24MatVecRange32) panel15Mode24MatVecRange64) panel15Mode24MatVecRange96) panel15Mode24MatVecRange128) row

theorem panel15Mode25MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .odd ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .odd ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode25MatVecRange0) panel15Mode25MatVecRange32) panel15Mode25MatVecRange64) panel15Mode25MatVecRange96) panel15Mode25MatVecRange128) row

theorem panel15Mode26MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .even ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .even ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode26MatVecRange0) panel15Mode26MatVecRange32) panel15Mode26MatVecRange64) panel15Mode26MatVecRange96) panel15Mode26MatVecRange128) row

theorem panel15Mode27MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .odd ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .odd ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode27MatVecRange0) panel15Mode27MatVecRange32) panel15Mode27MatVecRange64) panel15Mode27MatVecRange96) panel15Mode27MatVecRange128) row

theorem panel15Mode28MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .even ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .even ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode28MatVecRange0) panel15Mode28MatVecRange32) panel15Mode28MatVecRange64) panel15Mode28MatVecRange96) panel15Mode28MatVecRange128) row

theorem panel15Mode29MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .odd ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .odd ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode29MatVecRange0) panel15Mode29MatVecRange32) panel15Mode29MatVecRange64) panel15Mode29MatVecRange96) panel15Mode29MatVecRange128) row

theorem panel15Mode30MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .even ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .even ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode30MatVecRange0) panel15Mode30MatVecRange32) panel15Mode30MatVecRange64) panel15Mode30MatVecRange96) panel15Mode30MatVecRange128) row

theorem panel15Mode31MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .odd ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .odd ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode31MatVecRange0) panel15Mode31MatVecRange32) panel15Mode31MatVecRange64) panel15Mode31MatVecRange96) panel15Mode31MatVecRange128) row

theorem panel15Mode32MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .even ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .even ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode32MatVecRange0) panel15Mode32MatVecRange32) panel15Mode32MatVecRange64) panel15Mode32MatVecRange96) panel15Mode32MatVecRange128) row

theorem panel15Mode33MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .odd ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .odd ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode33MatVecRange0) panel15Mode33MatVecRange32) panel15Mode33MatVecRange64) panel15Mode33MatVecRange96) panel15Mode33MatVecRange128) row

theorem panel15Mode34MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .even ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .even ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode34MatVecRange0) panel15Mode34MatVecRange32) panel15Mode34MatVecRange64) panel15Mode34MatVecRange96) panel15Mode34MatVecRange128) row

theorem panel15Mode35MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .odd ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .odd ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode35MatVecRange0) panel15Mode35MatVecRange32) panel15Mode35MatVecRange64) panel15Mode35MatVecRange96) panel15Mode35MatVecRange128) row

theorem panel15Mode36MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .even ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .even ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode36MatVecRange0) panel15Mode36MatVecRange32) panel15Mode36MatVecRange64) panel15Mode36MatVecRange96) panel15Mode36MatVecRange128) row

theorem panel15Mode37MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .odd ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .odd ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode37MatVecRange0) panel15Mode37MatVecRange32) panel15Mode37MatVecRange64) panel15Mode37MatVecRange96) panel15Mode37MatVecRange128) row

theorem panel15Mode38MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .even ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .even ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode38MatVecRange0) panel15Mode38MatVecRange32) panel15Mode38MatVecRange64) panel15Mode38MatVecRange96) panel15Mode38MatVecRange128) row

theorem panel15Mode39MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .odd ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .odd ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode39MatVecRange0) panel15Mode39MatVecRange32) panel15Mode39MatVecRange64) panel15Mode39MatVecRange96) panel15Mode39MatVecRange128) row

theorem panel15Mode40MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .even ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .even ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode40MatVecRange0) panel15Mode40MatVecRange32) panel15Mode40MatVecRange64) panel15Mode40MatVecRange96) panel15Mode40MatVecRange128) row

theorem panel15Mode41MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .odd ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .odd ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode41MatVecRange0) panel15Mode41MatVecRange32) panel15Mode41MatVecRange64) panel15Mode41MatVecRange96) panel15Mode41MatVecRange128) row

theorem panel15Mode42MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .even ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .even ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode42MatVecRange0) panel15Mode42MatVecRange32) panel15Mode42MatVecRange64) panel15Mode42MatVecRange96) panel15Mode42MatVecRange128) row

theorem panel15Mode43MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .odd ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .odd ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode43MatVecRange0) panel15Mode43MatVecRange32) panel15Mode43MatVecRange64) panel15Mode43MatVecRange96) panel15Mode43MatVecRange128) row

theorem panel15Mode44MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .even ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .even ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode44MatVecRange0) panel15Mode44MatVecRange32) panel15Mode44MatVecRange64) panel15Mode44MatVecRange96) panel15Mode44MatVecRange128) row

theorem panel15Mode45MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .odd ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .odd ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode45MatVecRange0) panel15Mode45MatVecRange32) panel15Mode45MatVecRange64) panel15Mode45MatVecRange96) panel15Mode45MatVecRange128) row

theorem panel15Mode46MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .even ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .even ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode46MatVecRange0) panel15Mode46MatVecRange32) panel15Mode46MatVecRange64) panel15Mode46MatVecRange96) panel15Mode46MatVecRange128) row

theorem panel15Mode47MatVec_eq :
    P2RoundedFactorCheckpointData.panel15MomentData.matvecs
        .odd ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel15MomentData.moments
        (P2RoundedFactorCheckpointData.panel15FlatCache.component
          .odd ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel15Mode47MatVecRange0) panel15Mode47MatVecRange32) panel15Mode47MatVecRange64) panel15Mode47MatVecRange96) panel15Mode47MatVecRange128) row

theorem panel15MomentData_correct :
    P2RoundedFactorCheckpointData.panel15MomentData.CorrectFor
      P2RoundedFactorCheckpointData.panel15FlatCache := by
  apply PanelMomentData.CorrectFor.of_vector_eq
      panel15DefectMoments_eq panel15ComponentLengthLe
  intro kind i
  cases kind with
  | even =>
      fin_cases i
      · exact panel15Mode0MatVec_eq
      · exact panel15Mode2MatVec_eq
      · exact panel15Mode4MatVec_eq
      · exact panel15Mode6MatVec_eq
      · exact panel15Mode8MatVec_eq
      · exact panel15Mode10MatVec_eq
      · exact panel15Mode12MatVec_eq
      · exact panel15Mode14MatVec_eq
      · exact panel15Mode16MatVec_eq
      · exact panel15Mode18MatVec_eq
      · exact panel15Mode20MatVec_eq
      · exact panel15Mode22MatVec_eq
      · exact panel15Mode24MatVec_eq
      · exact panel15Mode26MatVec_eq
      · exact panel15Mode28MatVec_eq
      · exact panel15Mode30MatVec_eq
      · exact panel15Mode32MatVec_eq
      · exact panel15Mode34MatVec_eq
      · exact panel15Mode36MatVec_eq
      · exact panel15Mode38MatVec_eq
      · exact panel15Mode40MatVec_eq
      · exact panel15Mode42MatVec_eq
      · exact panel15Mode44MatVec_eq
      · exact panel15Mode46MatVec_eq
  | odd =>
      fin_cases i
      · exact panel15Mode1MatVec_eq
      · exact panel15Mode3MatVec_eq
      · exact panel15Mode5MatVec_eq
      · exact panel15Mode7MatVec_eq
      · exact panel15Mode9MatVec_eq
      · exact panel15Mode11MatVec_eq
      · exact panel15Mode13MatVec_eq
      · exact panel15Mode15MatVec_eq
      · exact panel15Mode17MatVec_eq
      · exact panel15Mode19MatVec_eq
      · exact panel15Mode21MatVec_eq
      · exact panel15Mode23MatVec_eq
      · exact panel15Mode25MatVec_eq
      · exact panel15Mode27MatVec_eq
      · exact panel15Mode29MatVec_eq
      · exact panel15Mode31MatVec_eq
      · exact panel15Mode33MatVec_eq
      · exact panel15Mode35MatVec_eq
      · exact panel15Mode37MatVec_eq
      · exact panel15Mode39MatVec_eq
      · exact panel15Mode41MatVec_eq
      · exact panel15Mode43MatVec_eq
      · exact panel15Mode45MatVec_eq
      · exact panel15Mode47MatVec_eq

end RHP2Bridge
