import RHBridge.P2RoundedFactorCheckpointData28

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel28FactorChunk8 :
    P2RoundedFactorCheckpointData.panel28Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨28, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel28Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨28, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel28Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨28, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel28Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨28, by decide⟩ := by
  decide +kernel

theorem panel28Prefix32_eq :
    P2RoundedFactorCheckpointData.panel28Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk8.1

theorem panel28Prefix33_eq :
    P2RoundedFactorCheckpointData.panel28Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk8.2.1

theorem panel28Prefix34_eq :
    P2RoundedFactorCheckpointData.panel28Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk8.2.2.1

theorem panel28Prefix35_eq :
    P2RoundedFactorCheckpointData.panel28Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk8.2.2.2

end RHP2Bridge
