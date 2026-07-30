import RHBridge.P2RoundedFactorCheckpointData16

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel16FactorChunk12 :
    P2RoundedFactorCheckpointData.panel16Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨16, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel16Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨16, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel16Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨16, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel16Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨16, by decide⟩ := by
  decide +kernel

theorem panel16Prefix48_eq :
    P2RoundedFactorCheckpointData.panel16Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk12.1

theorem panel16Prefix49_eq :
    P2RoundedFactorCheckpointData.panel16Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk12.2.1

theorem panel16Prefix50_eq :
    P2RoundedFactorCheckpointData.panel16Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk12.2.2.1

theorem panel16Prefix51_eq :
    P2RoundedFactorCheckpointData.panel16Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk12.2.2.2

end RHP2Bridge
