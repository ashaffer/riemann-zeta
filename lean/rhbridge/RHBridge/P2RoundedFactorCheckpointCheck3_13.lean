import RHBridge.P2RoundedFactorCheckpointData3

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel3FactorChunk13 :
    P2RoundedFactorCheckpointData.panel3Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨3, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel3Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨3, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel3Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨3, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel3Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨3, by decide⟩ := by
  decide +kernel

theorem panel3Prefix52_eq :
    P2RoundedFactorCheckpointData.panel3Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk13.1

theorem panel3Prefix53_eq :
    P2RoundedFactorCheckpointData.panel3Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk13.2.1

theorem panel3Prefix54_eq :
    P2RoundedFactorCheckpointData.panel3Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk13.2.2.1

theorem panel3Prefix55_eq :
    P2RoundedFactorCheckpointData.panel3Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk13.2.2.2

end RHP2Bridge
