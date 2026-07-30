import RHBridge.P2RoundedFactorCheckpointData16

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel16FactorChunk6 :
    P2RoundedFactorCheckpointData.panel16Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨16, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel16Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨16, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel16Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨16, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel16Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨16, by decide⟩ := by
  decide +kernel

theorem panel16Prefix24_eq :
    P2RoundedFactorCheckpointData.panel16Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk6.1

theorem panel16Prefix25_eq :
    P2RoundedFactorCheckpointData.panel16Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk6.2.1

theorem panel16Prefix26_eq :
    P2RoundedFactorCheckpointData.panel16Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk6.2.2.1

theorem panel16Prefix27_eq :
    P2RoundedFactorCheckpointData.panel16Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk6.2.2.2

end RHP2Bridge
