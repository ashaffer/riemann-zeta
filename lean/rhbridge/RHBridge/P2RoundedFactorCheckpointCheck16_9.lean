import RHBridge.P2RoundedFactorCheckpointData16

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel16FactorChunk9 :
    P2RoundedFactorCheckpointData.panel16Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨16, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel16Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨16, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel16Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨16, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel16Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨16, by decide⟩ := by
  decide +kernel

theorem panel16Prefix36_eq :
    P2RoundedFactorCheckpointData.panel16Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk9.1

theorem panel16Prefix37_eq :
    P2RoundedFactorCheckpointData.panel16Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk9.2.1

theorem panel16Prefix38_eq :
    P2RoundedFactorCheckpointData.panel16Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk9.2.2.1

theorem panel16Prefix39_eq :
    P2RoundedFactorCheckpointData.panel16Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk9.2.2.2

end RHP2Bridge
