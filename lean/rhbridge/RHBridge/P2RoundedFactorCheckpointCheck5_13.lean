import RHBridge.P2RoundedFactorCheckpointData5

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel5FactorChunk13 :
    P2RoundedFactorCheckpointData.panel5Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨5, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel5Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨5, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel5Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨5, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel5Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨5, by decide⟩ := by
  decide +kernel

theorem panel5Prefix52_eq :
    P2RoundedFactorCheckpointData.panel5Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk13.1

theorem panel5Prefix53_eq :
    P2RoundedFactorCheckpointData.panel5Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk13.2.1

theorem panel5Prefix54_eq :
    P2RoundedFactorCheckpointData.panel5Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk13.2.2.1

theorem panel5Prefix55_eq :
    P2RoundedFactorCheckpointData.panel5Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk13.2.2.2

end RHP2Bridge
