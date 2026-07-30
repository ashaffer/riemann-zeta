import RHBridge.P2RoundedFactorCheckpointData14

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14FactorChunk13 :
    P2RoundedFactorCheckpointData.panel14Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨14, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel14Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨14, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel14Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨14, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel14Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨14, by decide⟩ := by
  decide +kernel

theorem panel14Prefix52_eq :
    P2RoundedFactorCheckpointData.panel14Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk13.1

theorem panel14Prefix53_eq :
    P2RoundedFactorCheckpointData.panel14Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk13.2.1

theorem panel14Prefix54_eq :
    P2RoundedFactorCheckpointData.panel14Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk13.2.2.1

theorem panel14Prefix55_eq :
    P2RoundedFactorCheckpointData.panel14Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk13.2.2.2

end RHP2Bridge
