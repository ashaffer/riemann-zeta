import RHBridge.P2RoundedFactorCheckpointData23

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel23FactorChunk13 :
    P2RoundedFactorCheckpointData.panel23Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨23, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel23Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨23, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel23Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨23, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel23Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨23, by decide⟩ := by
  decide +kernel

theorem panel23Prefix52_eq :
    P2RoundedFactorCheckpointData.panel23Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk13.1

theorem panel23Prefix53_eq :
    P2RoundedFactorCheckpointData.panel23Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk13.2.1

theorem panel23Prefix54_eq :
    P2RoundedFactorCheckpointData.panel23Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk13.2.2.1

theorem panel23Prefix55_eq :
    P2RoundedFactorCheckpointData.panel23Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk13.2.2.2

end RHP2Bridge
