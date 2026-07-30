import RHBridge.P2RoundedFlatFactorCheckpoint26
import RHBridge.P2RoundedMomentLengths26
import RHBridge.P2RoundedMomentCheckpointCheck26_moments
import RHBridge.P2RoundedMomentCheckpointCheck26_mode0
import RHBridge.P2RoundedMomentCheckpointCheck26_mode1
import RHBridge.P2RoundedMomentCheckpointCheck26_mode2
import RHBridge.P2RoundedMomentCheckpointCheck26_mode3
import RHBridge.P2RoundedMomentCheckpointCheck26_mode4
import RHBridge.P2RoundedMomentCheckpointCheck26_mode5
import RHBridge.P2RoundedMomentCheckpointCheck26_mode6
import RHBridge.P2RoundedMomentCheckpointCheck26_mode7
import RHBridge.P2RoundedMomentCheckpointCheck26_mode8
import RHBridge.P2RoundedMomentCheckpointCheck26_mode9
import RHBridge.P2RoundedMomentCheckpointCheck26_mode10
import RHBridge.P2RoundedMomentCheckpointCheck26_mode11
import RHBridge.P2RoundedMomentCheckpointCheck26_mode12
import RHBridge.P2RoundedMomentCheckpointCheck26_mode13
import RHBridge.P2RoundedMomentCheckpointCheck26_mode14
import RHBridge.P2RoundedMomentCheckpointCheck26_mode15
import RHBridge.P2RoundedMomentCheckpointCheck26_mode16
import RHBridge.P2RoundedMomentCheckpointCheck26_mode17
import RHBridge.P2RoundedMomentCheckpointCheck26_mode18
import RHBridge.P2RoundedMomentCheckpointCheck26_mode19
import RHBridge.P2RoundedMomentCheckpointCheck26_mode20
import RHBridge.P2RoundedMomentCheckpointCheck26_mode21
import RHBridge.P2RoundedMomentCheckpointCheck26_mode22
import RHBridge.P2RoundedMomentCheckpointCheck26_mode23
import RHBridge.P2RoundedMomentCheckpointCheck26_mode24
import RHBridge.P2RoundedMomentCheckpointCheck26_mode25
import RHBridge.P2RoundedMomentCheckpointCheck26_mode26
import RHBridge.P2RoundedMomentCheckpointCheck26_mode27
import RHBridge.P2RoundedMomentCheckpointCheck26_mode28
import RHBridge.P2RoundedMomentCheckpointCheck26_mode29
import RHBridge.P2RoundedMomentCheckpointCheck26_mode30
import RHBridge.P2RoundedMomentCheckpointCheck26_mode31
import RHBridge.P2RoundedMomentCheckpointCheck26_mode32
import RHBridge.P2RoundedMomentCheckpointCheck26_mode33
import RHBridge.P2RoundedMomentCheckpointCheck26_mode34
import RHBridge.P2RoundedMomentCheckpointCheck26_mode35
import RHBridge.P2RoundedMomentCheckpointCheck26_mode36
import RHBridge.P2RoundedMomentCheckpointCheck26_mode37
import RHBridge.P2RoundedMomentCheckpointCheck26_mode38
import RHBridge.P2RoundedMomentCheckpointCheck26_mode39
import RHBridge.P2RoundedMomentCheckpointCheck26_mode40
import RHBridge.P2RoundedMomentCheckpointCheck26_mode41
import RHBridge.P2RoundedMomentCheckpointCheck26_mode42
import RHBridge.P2RoundedMomentCheckpointCheck26_mode43
import RHBridge.P2RoundedMomentCheckpointCheck26_mode44
import RHBridge.P2RoundedMomentCheckpointCheck26_mode45
import RHBridge.P2RoundedMomentCheckpointCheck26_mode46
import RHBridge.P2RoundedMomentCheckpointCheck26_mode47

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

theorem panel26DefectMoments_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.moments =
      P2RoundedTripleMoment.defectMoments
        P2RoundedFactorCheckpointData.panel26FlatCache.defect.coeffs := by
  apply vector_ext_fin
  intro row
  rw [P2RoundedTripleMoment.defectMoments_get]
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26DefectMomentRange0) panel26DefectMomentRange64) panel26DefectMomentRange128) panel26DefectMomentRange192) panel26DefectMomentRange256) row

theorem panel26Mode0MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .even ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .even ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode0MatVecRange0) panel26Mode0MatVecRange32) panel26Mode0MatVecRange64) panel26Mode0MatVecRange96) panel26Mode0MatVecRange128) row

theorem panel26Mode1MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .odd ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .odd ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode1MatVecRange0) panel26Mode1MatVecRange32) panel26Mode1MatVecRange64) panel26Mode1MatVecRange96) panel26Mode1MatVecRange128) row

theorem panel26Mode2MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .even ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .even ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode2MatVecRange0) panel26Mode2MatVecRange32) panel26Mode2MatVecRange64) panel26Mode2MatVecRange96) panel26Mode2MatVecRange128) row

theorem panel26Mode3MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .odd ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .odd ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode3MatVecRange0) panel26Mode3MatVecRange32) panel26Mode3MatVecRange64) panel26Mode3MatVecRange96) panel26Mode3MatVecRange128) row

theorem panel26Mode4MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .even ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .even ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode4MatVecRange0) panel26Mode4MatVecRange32) panel26Mode4MatVecRange64) panel26Mode4MatVecRange96) panel26Mode4MatVecRange128) row

theorem panel26Mode5MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .odd ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .odd ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode5MatVecRange0) panel26Mode5MatVecRange32) panel26Mode5MatVecRange64) panel26Mode5MatVecRange96) panel26Mode5MatVecRange128) row

theorem panel26Mode6MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .even ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .even ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode6MatVecRange0) panel26Mode6MatVecRange32) panel26Mode6MatVecRange64) panel26Mode6MatVecRange96) panel26Mode6MatVecRange128) row

theorem panel26Mode7MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .odd ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .odd ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode7MatVecRange0) panel26Mode7MatVecRange32) panel26Mode7MatVecRange64) panel26Mode7MatVecRange96) panel26Mode7MatVecRange128) row

theorem panel26Mode8MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .even ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .even ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode8MatVecRange0) panel26Mode8MatVecRange32) panel26Mode8MatVecRange64) panel26Mode8MatVecRange96) panel26Mode8MatVecRange128) row

theorem panel26Mode9MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .odd ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .odd ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode9MatVecRange0) panel26Mode9MatVecRange32) panel26Mode9MatVecRange64) panel26Mode9MatVecRange96) panel26Mode9MatVecRange128) row

theorem panel26Mode10MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .even ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .even ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode10MatVecRange0) panel26Mode10MatVecRange32) panel26Mode10MatVecRange64) panel26Mode10MatVecRange96) panel26Mode10MatVecRange128) row

theorem panel26Mode11MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .odd ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .odd ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode11MatVecRange0) panel26Mode11MatVecRange32) panel26Mode11MatVecRange64) panel26Mode11MatVecRange96) panel26Mode11MatVecRange128) row

theorem panel26Mode12MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .even ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .even ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode12MatVecRange0) panel26Mode12MatVecRange32) panel26Mode12MatVecRange64) panel26Mode12MatVecRange96) panel26Mode12MatVecRange128) row

theorem panel26Mode13MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .odd ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .odd ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode13MatVecRange0) panel26Mode13MatVecRange32) panel26Mode13MatVecRange64) panel26Mode13MatVecRange96) panel26Mode13MatVecRange128) row

theorem panel26Mode14MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .even ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .even ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode14MatVecRange0) panel26Mode14MatVecRange32) panel26Mode14MatVecRange64) panel26Mode14MatVecRange96) panel26Mode14MatVecRange128) row

theorem panel26Mode15MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .odd ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .odd ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode15MatVecRange0) panel26Mode15MatVecRange32) panel26Mode15MatVecRange64) panel26Mode15MatVecRange96) panel26Mode15MatVecRange128) row

theorem panel26Mode16MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .even ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .even ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode16MatVecRange0) panel26Mode16MatVecRange32) panel26Mode16MatVecRange64) panel26Mode16MatVecRange96) panel26Mode16MatVecRange128) row

theorem panel26Mode17MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .odd ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .odd ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode17MatVecRange0) panel26Mode17MatVecRange32) panel26Mode17MatVecRange64) panel26Mode17MatVecRange96) panel26Mode17MatVecRange128) row

theorem panel26Mode18MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .even ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .even ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode18MatVecRange0) panel26Mode18MatVecRange32) panel26Mode18MatVecRange64) panel26Mode18MatVecRange96) panel26Mode18MatVecRange128) row

theorem panel26Mode19MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .odd ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .odd ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode19MatVecRange0) panel26Mode19MatVecRange32) panel26Mode19MatVecRange64) panel26Mode19MatVecRange96) panel26Mode19MatVecRange128) row

theorem panel26Mode20MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .even ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .even ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode20MatVecRange0) panel26Mode20MatVecRange32) panel26Mode20MatVecRange64) panel26Mode20MatVecRange96) panel26Mode20MatVecRange128) row

theorem panel26Mode21MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .odd ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .odd ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode21MatVecRange0) panel26Mode21MatVecRange32) panel26Mode21MatVecRange64) panel26Mode21MatVecRange96) panel26Mode21MatVecRange128) row

theorem panel26Mode22MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .even ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .even ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode22MatVecRange0) panel26Mode22MatVecRange32) panel26Mode22MatVecRange64) panel26Mode22MatVecRange96) panel26Mode22MatVecRange128) row

theorem panel26Mode23MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .odd ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .odd ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode23MatVecRange0) panel26Mode23MatVecRange32) panel26Mode23MatVecRange64) panel26Mode23MatVecRange96) panel26Mode23MatVecRange128) row

theorem panel26Mode24MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .even ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .even ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode24MatVecRange0) panel26Mode24MatVecRange32) panel26Mode24MatVecRange64) panel26Mode24MatVecRange96) panel26Mode24MatVecRange128) row

theorem panel26Mode25MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .odd ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .odd ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode25MatVecRange0) panel26Mode25MatVecRange32) panel26Mode25MatVecRange64) panel26Mode25MatVecRange96) panel26Mode25MatVecRange128) row

theorem panel26Mode26MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .even ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .even ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode26MatVecRange0) panel26Mode26MatVecRange32) panel26Mode26MatVecRange64) panel26Mode26MatVecRange96) panel26Mode26MatVecRange128) row

theorem panel26Mode27MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .odd ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .odd ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode27MatVecRange0) panel26Mode27MatVecRange32) panel26Mode27MatVecRange64) panel26Mode27MatVecRange96) panel26Mode27MatVecRange128) row

theorem panel26Mode28MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .even ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .even ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode28MatVecRange0) panel26Mode28MatVecRange32) panel26Mode28MatVecRange64) panel26Mode28MatVecRange96) panel26Mode28MatVecRange128) row

theorem panel26Mode29MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .odd ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .odd ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode29MatVecRange0) panel26Mode29MatVecRange32) panel26Mode29MatVecRange64) panel26Mode29MatVecRange96) panel26Mode29MatVecRange128) row

theorem panel26Mode30MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .even ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .even ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode30MatVecRange0) panel26Mode30MatVecRange32) panel26Mode30MatVecRange64) panel26Mode30MatVecRange96) panel26Mode30MatVecRange128) row

theorem panel26Mode31MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .odd ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .odd ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode31MatVecRange0) panel26Mode31MatVecRange32) panel26Mode31MatVecRange64) panel26Mode31MatVecRange96) panel26Mode31MatVecRange128) row

theorem panel26Mode32MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .even ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .even ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode32MatVecRange0) panel26Mode32MatVecRange32) panel26Mode32MatVecRange64) panel26Mode32MatVecRange96) panel26Mode32MatVecRange128) row

theorem panel26Mode33MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .odd ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .odd ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode33MatVecRange0) panel26Mode33MatVecRange32) panel26Mode33MatVecRange64) panel26Mode33MatVecRange96) panel26Mode33MatVecRange128) row

theorem panel26Mode34MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .even ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .even ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode34MatVecRange0) panel26Mode34MatVecRange32) panel26Mode34MatVecRange64) panel26Mode34MatVecRange96) panel26Mode34MatVecRange128) row

theorem panel26Mode35MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .odd ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .odd ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode35MatVecRange0) panel26Mode35MatVecRange32) panel26Mode35MatVecRange64) panel26Mode35MatVecRange96) panel26Mode35MatVecRange128) row

theorem panel26Mode36MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .even ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .even ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode36MatVecRange0) panel26Mode36MatVecRange32) panel26Mode36MatVecRange64) panel26Mode36MatVecRange96) panel26Mode36MatVecRange128) row

theorem panel26Mode37MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .odd ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .odd ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode37MatVecRange0) panel26Mode37MatVecRange32) panel26Mode37MatVecRange64) panel26Mode37MatVecRange96) panel26Mode37MatVecRange128) row

theorem panel26Mode38MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .even ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .even ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode38MatVecRange0) panel26Mode38MatVecRange32) panel26Mode38MatVecRange64) panel26Mode38MatVecRange96) panel26Mode38MatVecRange128) row

theorem panel26Mode39MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .odd ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .odd ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode39MatVecRange0) panel26Mode39MatVecRange32) panel26Mode39MatVecRange64) panel26Mode39MatVecRange96) panel26Mode39MatVecRange128) row

theorem panel26Mode40MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .even ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .even ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode40MatVecRange0) panel26Mode40MatVecRange32) panel26Mode40MatVecRange64) panel26Mode40MatVecRange96) panel26Mode40MatVecRange128) row

theorem panel26Mode41MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .odd ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .odd ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode41MatVecRange0) panel26Mode41MatVecRange32) panel26Mode41MatVecRange64) panel26Mode41MatVecRange96) panel26Mode41MatVecRange128) row

theorem panel26Mode42MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .even ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .even ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode42MatVecRange0) panel26Mode42MatVecRange32) panel26Mode42MatVecRange64) panel26Mode42MatVecRange96) panel26Mode42MatVecRange128) row

theorem panel26Mode43MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .odd ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .odd ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode43MatVecRange0) panel26Mode43MatVecRange32) panel26Mode43MatVecRange64) panel26Mode43MatVecRange96) panel26Mode43MatVecRange128) row

theorem panel26Mode44MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .even ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .even ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode44MatVecRange0) panel26Mode44MatVecRange32) panel26Mode44MatVecRange64) panel26Mode44MatVecRange96) panel26Mode44MatVecRange128) row

theorem panel26Mode45MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .odd ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .odd ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode45MatVecRange0) panel26Mode45MatVecRange32) panel26Mode45MatVecRange64) panel26Mode45MatVecRange96) panel26Mode45MatVecRange128) row

theorem panel26Mode46MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .even ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .even ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode46MatVecRange0) panel26Mode46MatVecRange32) panel26Mode46MatVecRange64) panel26Mode46MatVecRange96) panel26Mode46MatVecRange128) row

theorem panel26Mode47MatVec_eq :
    P2RoundedFactorCheckpointData.panel26MomentData.matvecs
        .odd ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel26MomentData.moments
        (P2RoundedFactorCheckpointData.panel26FlatCache.component
          .odd ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel26Mode47MatVecRange0) panel26Mode47MatVecRange32) panel26Mode47MatVecRange64) panel26Mode47MatVecRange96) panel26Mode47MatVecRange128) row

theorem panel26MomentData_correct :
    P2RoundedFactorCheckpointData.panel26MomentData.CorrectFor
      P2RoundedFactorCheckpointData.panel26FlatCache := by
  apply PanelMomentData.CorrectFor.of_vector_eq
      panel26DefectMoments_eq panel26ComponentLengthLe
  intro kind i
  cases kind with
  | even =>
      fin_cases i
      · exact panel26Mode0MatVec_eq
      · exact panel26Mode2MatVec_eq
      · exact panel26Mode4MatVec_eq
      · exact panel26Mode6MatVec_eq
      · exact panel26Mode8MatVec_eq
      · exact panel26Mode10MatVec_eq
      · exact panel26Mode12MatVec_eq
      · exact panel26Mode14MatVec_eq
      · exact panel26Mode16MatVec_eq
      · exact panel26Mode18MatVec_eq
      · exact panel26Mode20MatVec_eq
      · exact panel26Mode22MatVec_eq
      · exact panel26Mode24MatVec_eq
      · exact panel26Mode26MatVec_eq
      · exact panel26Mode28MatVec_eq
      · exact panel26Mode30MatVec_eq
      · exact panel26Mode32MatVec_eq
      · exact panel26Mode34MatVec_eq
      · exact panel26Mode36MatVec_eq
      · exact panel26Mode38MatVec_eq
      · exact panel26Mode40MatVec_eq
      · exact panel26Mode42MatVec_eq
      · exact panel26Mode44MatVec_eq
      · exact panel26Mode46MatVec_eq
  | odd =>
      fin_cases i
      · exact panel26Mode1MatVec_eq
      · exact panel26Mode3MatVec_eq
      · exact panel26Mode5MatVec_eq
      · exact panel26Mode7MatVec_eq
      · exact panel26Mode9MatVec_eq
      · exact panel26Mode11MatVec_eq
      · exact panel26Mode13MatVec_eq
      · exact panel26Mode15MatVec_eq
      · exact panel26Mode17MatVec_eq
      · exact panel26Mode19MatVec_eq
      · exact panel26Mode21MatVec_eq
      · exact panel26Mode23MatVec_eq
      · exact panel26Mode25MatVec_eq
      · exact panel26Mode27MatVec_eq
      · exact panel26Mode29MatVec_eq
      · exact panel26Mode31MatVec_eq
      · exact panel26Mode33MatVec_eq
      · exact panel26Mode35MatVec_eq
      · exact panel26Mode37MatVec_eq
      · exact panel26Mode39MatVec_eq
      · exact panel26Mode41MatVec_eq
      · exact panel26Mode43MatVec_eq
      · exact panel26Mode45MatVec_eq
      · exact panel26Mode47MatVec_eq

end RHP2Bridge
