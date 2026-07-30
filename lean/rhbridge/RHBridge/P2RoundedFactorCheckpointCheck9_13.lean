import RHBridge.P2RoundedFactorCheckpointData9

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9FactorChunk13 :
    P2RoundedFactorCheckpointData.panel9Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨9, by decide⟩ := by
  decide +kernel

theorem panel9Prefix52_eq :
    P2RoundedFactorCheckpointData.panel9Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk13.1

theorem panel9Prefix53_eq :
    P2RoundedFactorCheckpointData.panel9Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk13.2.1

theorem panel9Prefix54_eq :
    P2RoundedFactorCheckpointData.panel9Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk13.2.2.1

theorem panel9Prefix55_eq :
    P2RoundedFactorCheckpointData.panel9Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk13.2.2.2

end RHP2Bridge
