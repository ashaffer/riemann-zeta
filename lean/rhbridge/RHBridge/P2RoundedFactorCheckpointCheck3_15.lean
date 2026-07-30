import RHBridge.P2RoundedFactorCheckpointData3

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel3FactorChunk15 :
    P2RoundedFactorCheckpointData.panel3Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨3, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel3Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨3, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel3Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨3, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel3Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨3, by decide⟩ := by
  decide +kernel

theorem panel3Prefix60_eq :
    P2RoundedFactorCheckpointData.panel3Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk15.1

theorem panel3Prefix61_eq :
    P2RoundedFactorCheckpointData.panel3Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk15.2.1

theorem panel3Prefix62_eq :
    P2RoundedFactorCheckpointData.panel3Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk15.2.2.1

theorem panel3Prefix63_eq :
    P2RoundedFactorCheckpointData.panel3Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk15.2.2.2

end RHP2Bridge
