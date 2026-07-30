import RHBridge.P2RoundedFactorCheckpointData3

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel3FactorChunk6 :
    P2RoundedFactorCheckpointData.panel3Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨3, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel3Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨3, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel3Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨3, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel3Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨3, by decide⟩ := by
  decide +kernel

theorem panel3Prefix24_eq :
    P2RoundedFactorCheckpointData.panel3Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk6.1

theorem panel3Prefix25_eq :
    P2RoundedFactorCheckpointData.panel3Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk6.2.1

theorem panel3Prefix26_eq :
    P2RoundedFactorCheckpointData.panel3Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk6.2.2.1

theorem panel3Prefix27_eq :
    P2RoundedFactorCheckpointData.panel3Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk6.2.2.2

end RHP2Bridge
