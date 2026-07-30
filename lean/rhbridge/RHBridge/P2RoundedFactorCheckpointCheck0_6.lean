import RHBridge.P2RoundedFactorCheckpointData0

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0FactorChunk6 :
    P2RoundedFactorCheckpointData.panel0Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨0, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel0Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨0, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel0Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨0, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel0Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨0, by decide⟩ := by
  decide +kernel

theorem panel0Prefix24_eq :
    P2RoundedFactorCheckpointData.panel0Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk6.1

theorem panel0Prefix25_eq :
    P2RoundedFactorCheckpointData.panel0Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk6.2.1

theorem panel0Prefix26_eq :
    P2RoundedFactorCheckpointData.panel0Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk6.2.2.1

theorem panel0Prefix27_eq :
    P2RoundedFactorCheckpointData.panel0Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk6.2.2.2

end RHP2Bridge
