import RHBridge.P2RoundedFactorCheckpointData15

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel15FactorChunk13 :
    P2RoundedFactorCheckpointData.panel15Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨15, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel15Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨15, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel15Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨15, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel15Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨15, by decide⟩ := by
  decide +kernel

theorem panel15Prefix52_eq :
    P2RoundedFactorCheckpointData.panel15Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk13.1

theorem panel15Prefix53_eq :
    P2RoundedFactorCheckpointData.panel15Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk13.2.1

theorem panel15Prefix54_eq :
    P2RoundedFactorCheckpointData.panel15Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk13.2.2.1

theorem panel15Prefix55_eq :
    P2RoundedFactorCheckpointData.panel15Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk13.2.2.2

end RHP2Bridge
