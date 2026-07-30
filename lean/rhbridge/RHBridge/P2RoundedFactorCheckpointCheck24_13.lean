import RHBridge.P2RoundedFactorCheckpointData24

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FactorChunk13 :
    P2RoundedFactorCheckpointData.panel24Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨24, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel24Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨24, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel24Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨24, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel24Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨24, by decide⟩ := by
  decide +kernel

theorem panel24Prefix52_eq :
    P2RoundedFactorCheckpointData.panel24Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk13.1

theorem panel24Prefix53_eq :
    P2RoundedFactorCheckpointData.panel24Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk13.2.1

theorem panel24Prefix54_eq :
    P2RoundedFactorCheckpointData.panel24Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk13.2.2.1

theorem panel24Prefix55_eq :
    P2RoundedFactorCheckpointData.panel24Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk13.2.2.2

end RHP2Bridge
