import RHBridge.P2RoundedFactorCheckpointData6

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel6FactorChunk6 :
    P2RoundedFactorCheckpointData.panel6Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨6, by decide⟩ := by
  decide +kernel

theorem panel6Prefix24_eq :
    P2RoundedFactorCheckpointData.panel6Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk6.1

theorem panel6Prefix25_eq :
    P2RoundedFactorCheckpointData.panel6Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk6.2.1

theorem panel6Prefix26_eq :
    P2RoundedFactorCheckpointData.panel6Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk6.2.2.1

theorem panel6Prefix27_eq :
    P2RoundedFactorCheckpointData.panel6Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk6.2.2.2

end RHP2Bridge
