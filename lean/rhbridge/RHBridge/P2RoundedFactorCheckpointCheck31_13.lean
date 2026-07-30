import RHBridge.P2RoundedFactorCheckpointData31

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel31FactorChunk13 :
    P2RoundedFactorCheckpointData.panel31Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨31, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel31Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨31, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel31Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨31, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel31Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨31, by decide⟩ := by
  decide +kernel

theorem panel31Prefix52_eq :
    P2RoundedFactorCheckpointData.panel31Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk13.1

theorem panel31Prefix53_eq :
    P2RoundedFactorCheckpointData.panel31Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk13.2.1

theorem panel31Prefix54_eq :
    P2RoundedFactorCheckpointData.panel31Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk13.2.2.1

theorem panel31Prefix55_eq :
    P2RoundedFactorCheckpointData.panel31Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk13.2.2.2

end RHP2Bridge
