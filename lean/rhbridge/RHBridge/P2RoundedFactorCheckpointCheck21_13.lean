import RHBridge.P2RoundedFactorCheckpointData21

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel21FactorChunk13 :
    P2RoundedFactorCheckpointData.panel21Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨21, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel21Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨21, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel21Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨21, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel21Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨21, by decide⟩ := by
  decide +kernel

theorem panel21Prefix52_eq :
    P2RoundedFactorCheckpointData.panel21Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk13.1

theorem panel21Prefix53_eq :
    P2RoundedFactorCheckpointData.panel21Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk13.2.1

theorem panel21Prefix54_eq :
    P2RoundedFactorCheckpointData.panel21Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk13.2.2.1

theorem panel21Prefix55_eq :
    P2RoundedFactorCheckpointData.panel21Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk13.2.2.2

end RHP2Bridge
