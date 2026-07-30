import RHBridge.P2RoundedFactorCheckpointData3

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel3FactorChunk9 :
    P2RoundedFactorCheckpointData.panel3Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨3, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel3Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨3, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel3Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨3, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel3Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨3, by decide⟩ := by
  decide +kernel

theorem panel3Prefix36_eq :
    P2RoundedFactorCheckpointData.panel3Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk9.1

theorem panel3Prefix37_eq :
    P2RoundedFactorCheckpointData.panel3Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk9.2.1

theorem panel3Prefix38_eq :
    P2RoundedFactorCheckpointData.panel3Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk9.2.2.1

theorem panel3Prefix39_eq :
    P2RoundedFactorCheckpointData.panel3Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk9.2.2.2

end RHP2Bridge
