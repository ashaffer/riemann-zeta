import RHBridge.P2RoundedFlatFactorCheckpoint13
import RHBridge.P2RoundedMomentLengths13
import RHBridge.P2RoundedMomentCheckpointCheck13_moments
import RHBridge.P2RoundedMomentCheckpointCheck13_mode0
import RHBridge.P2RoundedMomentCheckpointCheck13_mode1
import RHBridge.P2RoundedMomentCheckpointCheck13_mode2
import RHBridge.P2RoundedMomentCheckpointCheck13_mode3
import RHBridge.P2RoundedMomentCheckpointCheck13_mode4
import RHBridge.P2RoundedMomentCheckpointCheck13_mode5
import RHBridge.P2RoundedMomentCheckpointCheck13_mode6
import RHBridge.P2RoundedMomentCheckpointCheck13_mode7
import RHBridge.P2RoundedMomentCheckpointCheck13_mode8
import RHBridge.P2RoundedMomentCheckpointCheck13_mode9
import RHBridge.P2RoundedMomentCheckpointCheck13_mode10
import RHBridge.P2RoundedMomentCheckpointCheck13_mode11
import RHBridge.P2RoundedMomentCheckpointCheck13_mode12
import RHBridge.P2RoundedMomentCheckpointCheck13_mode13
import RHBridge.P2RoundedMomentCheckpointCheck13_mode14
import RHBridge.P2RoundedMomentCheckpointCheck13_mode15
import RHBridge.P2RoundedMomentCheckpointCheck13_mode16
import RHBridge.P2RoundedMomentCheckpointCheck13_mode17
import RHBridge.P2RoundedMomentCheckpointCheck13_mode18
import RHBridge.P2RoundedMomentCheckpointCheck13_mode19
import RHBridge.P2RoundedMomentCheckpointCheck13_mode20
import RHBridge.P2RoundedMomentCheckpointCheck13_mode21
import RHBridge.P2RoundedMomentCheckpointCheck13_mode22
import RHBridge.P2RoundedMomentCheckpointCheck13_mode23
import RHBridge.P2RoundedMomentCheckpointCheck13_mode24
import RHBridge.P2RoundedMomentCheckpointCheck13_mode25
import RHBridge.P2RoundedMomentCheckpointCheck13_mode26
import RHBridge.P2RoundedMomentCheckpointCheck13_mode27
import RHBridge.P2RoundedMomentCheckpointCheck13_mode28
import RHBridge.P2RoundedMomentCheckpointCheck13_mode29
import RHBridge.P2RoundedMomentCheckpointCheck13_mode30
import RHBridge.P2RoundedMomentCheckpointCheck13_mode31
import RHBridge.P2RoundedMomentCheckpointCheck13_mode32
import RHBridge.P2RoundedMomentCheckpointCheck13_mode33
import RHBridge.P2RoundedMomentCheckpointCheck13_mode34
import RHBridge.P2RoundedMomentCheckpointCheck13_mode35
import RHBridge.P2RoundedMomentCheckpointCheck13_mode36
import RHBridge.P2RoundedMomentCheckpointCheck13_mode37
import RHBridge.P2RoundedMomentCheckpointCheck13_mode38
import RHBridge.P2RoundedMomentCheckpointCheck13_mode39
import RHBridge.P2RoundedMomentCheckpointCheck13_mode40
import RHBridge.P2RoundedMomentCheckpointCheck13_mode41
import RHBridge.P2RoundedMomentCheckpointCheck13_mode42
import RHBridge.P2RoundedMomentCheckpointCheck13_mode43
import RHBridge.P2RoundedMomentCheckpointCheck13_mode44
import RHBridge.P2RoundedMomentCheckpointCheck13_mode45
import RHBridge.P2RoundedMomentCheckpointCheck13_mode46
import RHBridge.P2RoundedMomentCheckpointCheck13_mode47

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

theorem panel13DefectMoments_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.moments =
      P2RoundedTripleMoment.defectMoments
        P2RoundedFactorCheckpointData.panel13FlatCache.defect.coeffs := by
  apply vector_ext_fin
  intro row
  rw [P2RoundedTripleMoment.defectMoments_get]
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13DefectMomentRange0) panel13DefectMomentRange64) panel13DefectMomentRange128) panel13DefectMomentRange192) panel13DefectMomentRange256) row

theorem panel13Mode0MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .even ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .even ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode0MatVecRange0) panel13Mode0MatVecRange32) panel13Mode0MatVecRange64) panel13Mode0MatVecRange96) panel13Mode0MatVecRange128) row

theorem panel13Mode1MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .odd ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .odd ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode1MatVecRange0) panel13Mode1MatVecRange32) panel13Mode1MatVecRange64) panel13Mode1MatVecRange96) panel13Mode1MatVecRange128) row

theorem panel13Mode2MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .even ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .even ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode2MatVecRange0) panel13Mode2MatVecRange32) panel13Mode2MatVecRange64) panel13Mode2MatVecRange96) panel13Mode2MatVecRange128) row

theorem panel13Mode3MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .odd ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .odd ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode3MatVecRange0) panel13Mode3MatVecRange32) panel13Mode3MatVecRange64) panel13Mode3MatVecRange96) panel13Mode3MatVecRange128) row

theorem panel13Mode4MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .even ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .even ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode4MatVecRange0) panel13Mode4MatVecRange32) panel13Mode4MatVecRange64) panel13Mode4MatVecRange96) panel13Mode4MatVecRange128) row

theorem panel13Mode5MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .odd ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .odd ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode5MatVecRange0) panel13Mode5MatVecRange32) panel13Mode5MatVecRange64) panel13Mode5MatVecRange96) panel13Mode5MatVecRange128) row

theorem panel13Mode6MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .even ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .even ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode6MatVecRange0) panel13Mode6MatVecRange32) panel13Mode6MatVecRange64) panel13Mode6MatVecRange96) panel13Mode6MatVecRange128) row

theorem panel13Mode7MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .odd ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .odd ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode7MatVecRange0) panel13Mode7MatVecRange32) panel13Mode7MatVecRange64) panel13Mode7MatVecRange96) panel13Mode7MatVecRange128) row

theorem panel13Mode8MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .even ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .even ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode8MatVecRange0) panel13Mode8MatVecRange32) panel13Mode8MatVecRange64) panel13Mode8MatVecRange96) panel13Mode8MatVecRange128) row

theorem panel13Mode9MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .odd ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .odd ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode9MatVecRange0) panel13Mode9MatVecRange32) panel13Mode9MatVecRange64) panel13Mode9MatVecRange96) panel13Mode9MatVecRange128) row

theorem panel13Mode10MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .even ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .even ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode10MatVecRange0) panel13Mode10MatVecRange32) panel13Mode10MatVecRange64) panel13Mode10MatVecRange96) panel13Mode10MatVecRange128) row

theorem panel13Mode11MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .odd ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .odd ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode11MatVecRange0) panel13Mode11MatVecRange32) panel13Mode11MatVecRange64) panel13Mode11MatVecRange96) panel13Mode11MatVecRange128) row

theorem panel13Mode12MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .even ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .even ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode12MatVecRange0) panel13Mode12MatVecRange32) panel13Mode12MatVecRange64) panel13Mode12MatVecRange96) panel13Mode12MatVecRange128) row

theorem panel13Mode13MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .odd ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .odd ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode13MatVecRange0) panel13Mode13MatVecRange32) panel13Mode13MatVecRange64) panel13Mode13MatVecRange96) panel13Mode13MatVecRange128) row

theorem panel13Mode14MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .even ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .even ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode14MatVecRange0) panel13Mode14MatVecRange32) panel13Mode14MatVecRange64) panel13Mode14MatVecRange96) panel13Mode14MatVecRange128) row

theorem panel13Mode15MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .odd ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .odd ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode15MatVecRange0) panel13Mode15MatVecRange32) panel13Mode15MatVecRange64) panel13Mode15MatVecRange96) panel13Mode15MatVecRange128) row

theorem panel13Mode16MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .even ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .even ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode16MatVecRange0) panel13Mode16MatVecRange32) panel13Mode16MatVecRange64) panel13Mode16MatVecRange96) panel13Mode16MatVecRange128) row

theorem panel13Mode17MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .odd ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .odd ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode17MatVecRange0) panel13Mode17MatVecRange32) panel13Mode17MatVecRange64) panel13Mode17MatVecRange96) panel13Mode17MatVecRange128) row

theorem panel13Mode18MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .even ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .even ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode18MatVecRange0) panel13Mode18MatVecRange32) panel13Mode18MatVecRange64) panel13Mode18MatVecRange96) panel13Mode18MatVecRange128) row

theorem panel13Mode19MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .odd ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .odd ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode19MatVecRange0) panel13Mode19MatVecRange32) panel13Mode19MatVecRange64) panel13Mode19MatVecRange96) panel13Mode19MatVecRange128) row

theorem panel13Mode20MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .even ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .even ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode20MatVecRange0) panel13Mode20MatVecRange32) panel13Mode20MatVecRange64) panel13Mode20MatVecRange96) panel13Mode20MatVecRange128) row

theorem panel13Mode21MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .odd ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .odd ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode21MatVecRange0) panel13Mode21MatVecRange32) panel13Mode21MatVecRange64) panel13Mode21MatVecRange96) panel13Mode21MatVecRange128) row

theorem panel13Mode22MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .even ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .even ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode22MatVecRange0) panel13Mode22MatVecRange32) panel13Mode22MatVecRange64) panel13Mode22MatVecRange96) panel13Mode22MatVecRange128) row

theorem panel13Mode23MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .odd ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .odd ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode23MatVecRange0) panel13Mode23MatVecRange32) panel13Mode23MatVecRange64) panel13Mode23MatVecRange96) panel13Mode23MatVecRange128) row

theorem panel13Mode24MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .even ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .even ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode24MatVecRange0) panel13Mode24MatVecRange32) panel13Mode24MatVecRange64) panel13Mode24MatVecRange96) panel13Mode24MatVecRange128) row

theorem panel13Mode25MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .odd ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .odd ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode25MatVecRange0) panel13Mode25MatVecRange32) panel13Mode25MatVecRange64) panel13Mode25MatVecRange96) panel13Mode25MatVecRange128) row

theorem panel13Mode26MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .even ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .even ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode26MatVecRange0) panel13Mode26MatVecRange32) panel13Mode26MatVecRange64) panel13Mode26MatVecRange96) panel13Mode26MatVecRange128) row

theorem panel13Mode27MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .odd ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .odd ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode27MatVecRange0) panel13Mode27MatVecRange32) panel13Mode27MatVecRange64) panel13Mode27MatVecRange96) panel13Mode27MatVecRange128) row

theorem panel13Mode28MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .even ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .even ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode28MatVecRange0) panel13Mode28MatVecRange32) panel13Mode28MatVecRange64) panel13Mode28MatVecRange96) panel13Mode28MatVecRange128) row

theorem panel13Mode29MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .odd ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .odd ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode29MatVecRange0) panel13Mode29MatVecRange32) panel13Mode29MatVecRange64) panel13Mode29MatVecRange96) panel13Mode29MatVecRange128) row

theorem panel13Mode30MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .even ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .even ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode30MatVecRange0) panel13Mode30MatVecRange32) panel13Mode30MatVecRange64) panel13Mode30MatVecRange96) panel13Mode30MatVecRange128) row

theorem panel13Mode31MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .odd ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .odd ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode31MatVecRange0) panel13Mode31MatVecRange32) panel13Mode31MatVecRange64) panel13Mode31MatVecRange96) panel13Mode31MatVecRange128) row

theorem panel13Mode32MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .even ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .even ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode32MatVecRange0) panel13Mode32MatVecRange32) panel13Mode32MatVecRange64) panel13Mode32MatVecRange96) panel13Mode32MatVecRange128) row

theorem panel13Mode33MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .odd ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .odd ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode33MatVecRange0) panel13Mode33MatVecRange32) panel13Mode33MatVecRange64) panel13Mode33MatVecRange96) panel13Mode33MatVecRange128) row

theorem panel13Mode34MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .even ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .even ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode34MatVecRange0) panel13Mode34MatVecRange32) panel13Mode34MatVecRange64) panel13Mode34MatVecRange96) panel13Mode34MatVecRange128) row

theorem panel13Mode35MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .odd ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .odd ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode35MatVecRange0) panel13Mode35MatVecRange32) panel13Mode35MatVecRange64) panel13Mode35MatVecRange96) panel13Mode35MatVecRange128) row

theorem panel13Mode36MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .even ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .even ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode36MatVecRange0) panel13Mode36MatVecRange32) panel13Mode36MatVecRange64) panel13Mode36MatVecRange96) panel13Mode36MatVecRange128) row

theorem panel13Mode37MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .odd ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .odd ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode37MatVecRange0) panel13Mode37MatVecRange32) panel13Mode37MatVecRange64) panel13Mode37MatVecRange96) panel13Mode37MatVecRange128) row

theorem panel13Mode38MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .even ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .even ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode38MatVecRange0) panel13Mode38MatVecRange32) panel13Mode38MatVecRange64) panel13Mode38MatVecRange96) panel13Mode38MatVecRange128) row

theorem panel13Mode39MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .odd ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .odd ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode39MatVecRange0) panel13Mode39MatVecRange32) panel13Mode39MatVecRange64) panel13Mode39MatVecRange96) panel13Mode39MatVecRange128) row

theorem panel13Mode40MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .even ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .even ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode40MatVecRange0) panel13Mode40MatVecRange32) panel13Mode40MatVecRange64) panel13Mode40MatVecRange96) panel13Mode40MatVecRange128) row

theorem panel13Mode41MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .odd ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .odd ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode41MatVecRange0) panel13Mode41MatVecRange32) panel13Mode41MatVecRange64) panel13Mode41MatVecRange96) panel13Mode41MatVecRange128) row

theorem panel13Mode42MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .even ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .even ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode42MatVecRange0) panel13Mode42MatVecRange32) panel13Mode42MatVecRange64) panel13Mode42MatVecRange96) panel13Mode42MatVecRange128) row

theorem panel13Mode43MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .odd ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .odd ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode43MatVecRange0) panel13Mode43MatVecRange32) panel13Mode43MatVecRange64) panel13Mode43MatVecRange96) panel13Mode43MatVecRange128) row

theorem panel13Mode44MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .even ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .even ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode44MatVecRange0) panel13Mode44MatVecRange32) panel13Mode44MatVecRange64) panel13Mode44MatVecRange96) panel13Mode44MatVecRange128) row

theorem panel13Mode45MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .odd ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .odd ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode45MatVecRange0) panel13Mode45MatVecRange32) panel13Mode45MatVecRange64) panel13Mode45MatVecRange96) panel13Mode45MatVecRange128) row

theorem panel13Mode46MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .even ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .even ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode46MatVecRange0) panel13Mode46MatVecRange32) panel13Mode46MatVecRange64) panel13Mode46MatVecRange96) panel13Mode46MatVecRange128) row

theorem panel13Mode47MatVec_eq :
    P2RoundedFactorCheckpointData.panel13MomentData.matvecs
        .odd ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel13MomentData.moments
        (P2RoundedFactorCheckpointData.panel13FlatCache.component
          .odd ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel13Mode47MatVecRange0) panel13Mode47MatVecRange32) panel13Mode47MatVecRange64) panel13Mode47MatVecRange96) panel13Mode47MatVecRange128) row

theorem panel13MomentData_correct :
    P2RoundedFactorCheckpointData.panel13MomentData.CorrectFor
      P2RoundedFactorCheckpointData.panel13FlatCache := by
  apply PanelMomentData.CorrectFor.of_vector_eq
      panel13DefectMoments_eq panel13ComponentLengthLe
  intro kind i
  cases kind with
  | even =>
      fin_cases i
      · exact panel13Mode0MatVec_eq
      · exact panel13Mode2MatVec_eq
      · exact panel13Mode4MatVec_eq
      · exact panel13Mode6MatVec_eq
      · exact panel13Mode8MatVec_eq
      · exact panel13Mode10MatVec_eq
      · exact panel13Mode12MatVec_eq
      · exact panel13Mode14MatVec_eq
      · exact panel13Mode16MatVec_eq
      · exact panel13Mode18MatVec_eq
      · exact panel13Mode20MatVec_eq
      · exact panel13Mode22MatVec_eq
      · exact panel13Mode24MatVec_eq
      · exact panel13Mode26MatVec_eq
      · exact panel13Mode28MatVec_eq
      · exact panel13Mode30MatVec_eq
      · exact panel13Mode32MatVec_eq
      · exact panel13Mode34MatVec_eq
      · exact panel13Mode36MatVec_eq
      · exact panel13Mode38MatVec_eq
      · exact panel13Mode40MatVec_eq
      · exact panel13Mode42MatVec_eq
      · exact panel13Mode44MatVec_eq
      · exact panel13Mode46MatVec_eq
  | odd =>
      fin_cases i
      · exact panel13Mode1MatVec_eq
      · exact panel13Mode3MatVec_eq
      · exact panel13Mode5MatVec_eq
      · exact panel13Mode7MatVec_eq
      · exact panel13Mode9MatVec_eq
      · exact panel13Mode11MatVec_eq
      · exact panel13Mode13MatVec_eq
      · exact panel13Mode15MatVec_eq
      · exact panel13Mode17MatVec_eq
      · exact panel13Mode19MatVec_eq
      · exact panel13Mode21MatVec_eq
      · exact panel13Mode23MatVec_eq
      · exact panel13Mode25MatVec_eq
      · exact panel13Mode27MatVec_eq
      · exact panel13Mode29MatVec_eq
      · exact panel13Mode31MatVec_eq
      · exact panel13Mode33MatVec_eq
      · exact panel13Mode35MatVec_eq
      · exact panel13Mode37MatVec_eq
      · exact panel13Mode39MatVec_eq
      · exact panel13Mode41MatVec_eq
      · exact panel13Mode43MatVec_eq
      · exact panel13Mode45MatVec_eq
      · exact panel13Mode47MatVec_eq

end RHP2Bridge
