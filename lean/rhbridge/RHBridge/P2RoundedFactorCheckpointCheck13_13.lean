import RHBridge.P2RoundedFactorCheckpointData13

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel13FactorChunk13 :
    P2RoundedFactorCheckpointData.panel13Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨13, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel13Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨13, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel13Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨13, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel13Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨13, by decide⟩ := by
  decide +kernel

theorem panel13Prefix52_eq :
    P2RoundedFactorCheckpointData.panel13Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk13.1

theorem panel13Prefix53_eq :
    P2RoundedFactorCheckpointData.panel13Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk13.2.1

theorem panel13Prefix54_eq :
    P2RoundedFactorCheckpointData.panel13Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk13.2.2.1

theorem panel13Prefix55_eq :
    P2RoundedFactorCheckpointData.panel13Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk13.2.2.2

end RHP2Bridge
