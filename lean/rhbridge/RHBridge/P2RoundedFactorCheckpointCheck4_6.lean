import RHBridge.P2RoundedFactorCheckpointData4

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel4FactorChunk6 :
    P2RoundedFactorCheckpointData.panel4Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨4, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel4Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨4, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel4Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨4, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel4Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨4, by decide⟩ := by
  decide +kernel

theorem panel4Prefix24_eq :
    P2RoundedFactorCheckpointData.panel4Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk6.1

theorem panel4Prefix25_eq :
    P2RoundedFactorCheckpointData.panel4Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk6.2.1

theorem panel4Prefix26_eq :
    P2RoundedFactorCheckpointData.panel4Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk6.2.2.1

theorem panel4Prefix27_eq :
    P2RoundedFactorCheckpointData.panel4Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk6.2.2.2

end RHP2Bridge
