import RHBridge.P2RoundedFactorCheckpointData12

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12FactorChunk13 :
    P2RoundedFactorCheckpointData.panel12Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨12, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel12Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨12, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel12Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨12, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel12Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨12, by decide⟩ := by
  decide +kernel

theorem panel12Prefix52_eq :
    P2RoundedFactorCheckpointData.panel12Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk13.1

theorem panel12Prefix53_eq :
    P2RoundedFactorCheckpointData.panel12Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk13.2.1

theorem panel12Prefix54_eq :
    P2RoundedFactorCheckpointData.panel12Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk13.2.2.1

theorem panel12Prefix55_eq :
    P2RoundedFactorCheckpointData.panel12Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk13.2.2.2

end RHP2Bridge
